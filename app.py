from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def inicio():
    if request.method == "POST":
        nombre = request.form["nombre"]
        telefono = request.form["telefono"]
        mensaje = request.form["mensaje"]
        fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open("mensajes.txt", "a", encoding="utf-8") as archivo:
            archivo.write(f"\nFecha: {fecha}\n")
            archivo.write(f"Nombre: {nombre}\n")
            archivo.write(f"Teléfono: {telefono}\n")
            archivo.write(f"Mensaje: {mensaje}\n")
            archivo.write("-" * 40)

        print("Mensaje guardado correctamente")

    return render_template("index.html")

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
    