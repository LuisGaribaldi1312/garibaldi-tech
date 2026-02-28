from flask import Flask, render_template, request
import datetime
import os
import requests
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Text, DateTime
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import insert as sa_insert

# Database setup: use DATABASE_URL env var (Postgres on Railway) or local SQLite fallback
DB_URL = os.environ.get("DATABASE_URL")
if not DB_URL:
    # local sqlite file
    DB_URL = f"sqlite:///{os.path.join(os.getcwd(), 'mensajes.db')}"

if DB_URL.startswith("sqlite:///"):
    engine = create_engine(DB_URL, connect_args={"check_same_thread": False})
else:
    engine = create_engine(DB_URL)

metadata = MetaData()
messages_table = Table(
    "messages",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("fecha", DateTime),
    Column("nombre", String(200)),
    Column("telefono", String(50)),
    Column("mensaje", Text),
)

metadata.create_all(engine)

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def inicio():
    if request.method == "POST":
        nombre = request.form["nombre"]
        telefono = request.form["telefono"]
        mensaje = request.form["mensaje"]
        fecha = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        mensajes_path = os.path.join(os.getcwd(), "mensajes.txt")
        with open(mensajes_path, "a", encoding="utf-8") as archivo:
            archivo.write(f"\nFecha: {fecha}\n")
            archivo.write(f"Nombre: {nombre}\n")
            archivo.write(f"Teléfono: {telefono}\n")
            archivo.write(f"Mensaje: {mensaje}\n")
            archivo.write("-" * 40 + "\n")

        print("Mensaje guardado correctamente en", mensajes_path)

        # Enviar notificación a Telegram si está configurado
        tg_token = os.environ.get("TELEGRAM_TOKEN")
        tg_chat = os.environ.get("TELEGRAM_CHAT_ID")
        if tg_token and tg_chat:
            try:
                text = f"Nuevo mensaje ({fecha})\nNombre: {nombre}\nTel: {telefono}\nMensaje: {mensaje}"
                resp = requests.post(
                    f"https://api.telegram.org/bot{tg_token}/sendMessage",
                    data={"chat_id": tg_chat, "text": text}
                )
                if resp.status_code == 200:
                    print("Notificación enviada por Telegram")
                else:
                    print("Error Telegram:", resp.status_code, resp.text)
            except Exception as e:
                print("Excepción al enviar Telegram:", e)

        # Enviar mensaje por WhatsApp vía Twilio si está configurado
        tw_sid = os.environ.get("TWILIO_ACCOUNT_SID")
        tw_token = os.environ.get("TWILIO_AUTH_TOKEN")
        tw_from = os.environ.get("TWILIO_WHATSAPP_FROM")
        tw_to = os.environ.get("WHATSAPP_TO")
        if tw_sid and tw_token and tw_from and tw_to:
            try:
                tw_url = f"https://api.twilio.com/2010-04-01/Accounts/{tw_sid}/Messages.json"
                body = f"Nuevo mensaje ({fecha})\nNombre: {nombre}\nTel: {telefono}\nMensaje: {mensaje}"
                resp = requests.post(
                    tw_url,
                    auth=(tw_sid, tw_token),
                    data={"From": tw_from, "To": tw_to, "Body": body},
                )
                if resp.status_code in (200, 201):
                    print("Mensaje enviado por WhatsApp/Twilio")
                else:
                    print("Error Twilio:", resp.status_code, resp.text)
            except Exception as e:
                print("Excepción al enviar Twilio:", e)

        # Guardar en la base de datos (si está disponible)
        try:
            with engine.begin() as conn:
                conn.execute(
                    sa_insert(messages_table).values(
                        fecha=datetime.datetime.now(), nombre=nombre, telefono=telefono, mensaje=mensaje
                    )
                )
            print("Mensaje guardado en la base de datos")
        except SQLAlchemyError as e:
            print("Error al guardar en la DB:", e)

    return render_template("index.html")

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
    