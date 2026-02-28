# Garibaldi Web

Pequeña aplicación Flask para recibir mensajes desde un formulario y guardarlos en `mensajes.txt`.

Requisitos
- Python 3.10+ (o la versión que tengas instalada)
- Virtualenv recomendado

Instalación y ejecución (Windows)

1. Crear y activar entorno virtual:

```powershell
python -m venv venv
venv\Scripts\Activate.ps1
```

2. Instalar dependencias:

```powershell
python -m pip install -r requirements.txt
```

3. Ejecutar la aplicación (modo desarrollo):

```powershell
python -m flask --app app --debug run
```

4. Abrir en el navegador: `http://127.0.0.1:5000`

Uso
- Rellenar el formulario de contacto en la página. Las entradas se guardan en `mensajes.txt`.

Git — commit y push

Si aún no tienes remoto configurado, añade tu remoto y empuja la rama `main`:

```powershell
git remote add origin https://github.com/<TU_USUARIO>/garibaldi-tech.git
git branch -M main
git push -u origin main
```

Nota de seguridad
- No incluyas tokens ni contraseñas en el repositorio.

Contacto
- Si quieres, puedo añadir más instrucciones (despliegue, env vars, Docker).

Notificaciones por Telegram (opcional)
- Puedes recibir los mensajes directamente en Telegram creando un bot y configurando dos variables de entorno en tu servicio (Render/Railway/Heroku):
	- `TELEGRAM_TOKEN` → token del bot (BotFather)
	- `TELEGRAM_CHAT_ID` → id del chat o tu id de Telegram
- El servidor ya envía una notificación a Telegram si estas variables están configuradas.
