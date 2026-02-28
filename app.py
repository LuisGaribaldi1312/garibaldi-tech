from flask import Flask, render_template, request
from datetime import datetime
import os
import requests

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def inicio():
    if request.method == "POST":
        nombre = request.form["nombre"]
        telefono = request.form["telefono"]
        mensaje = request.form["mensaje"]
        fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
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

    return render_template("index.html")

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
    