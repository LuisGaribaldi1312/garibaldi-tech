from flask import Flask, render_template, request
from datetime import datetime
import os

app = Flask(__name__)

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

        try:
            with open(mensajes_path, "a", encoding="utf-8") as archivo:
                archivo.write(f"\nFecha: {fecha}\n")
                archivo.write(f"Nombre: {nombre}\n")
                archivo.write(f"Teléfono: {telefono}\n")
                archivo.write(f"Mensaje: {mensaje}\n")
                archivo.write("-" * 40 + "\n")
            print("Mensaje guardado correctamente en", mensajes_path)
        except Exception as e:
            print("Error guardando mensaje:", e)

    return render_template("index.html")

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
    