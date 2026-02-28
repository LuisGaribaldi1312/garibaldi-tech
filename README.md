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

Notificaciones por WhatsApp (opcional, vía Twilio)
- Puedes recibir los mensajes en WhatsApp usando Twilio. Pasos resumidos:
	1. Crea cuenta en https://www.twilio.com y ve a Messaging → Try WhatsApp → Sandbox.
	2. Sigue las instrucciones para unir tu número al sandbox (enviar el código por WhatsApp).
	3. Obtén `Account SID` y `Auth Token` desde la consola de Twilio.
	4. En GitHub/Render/Railway/Heroku añade las variables de entorno:
		 - `TWILIO_ACCOUNT_SID` = tu Account SID
		 - `TWILIO_AUTH_TOKEN` = tu Auth Token
		 - `TWILIO_WHATSAPP_FROM` = el número de Twilio en formato `whatsapp:+1415...` (sandbox)
		 - `WHATSAPP_TO` = tu número destino en formato `whatsapp:+52XXXXXXXXXX`
	5. Fuerza un redeploy del servicio; los mensajes se enviarán a WhatsApp cuando los usuarios usen el formulario.

Almacenamiento persistente (recomendado)
- Recomendado: provisiona una base de datos PostgreSQL (por ejemplo en Railway) y configura la variable de entorno `DATABASE_URL` con la URL de conexión. El servidor guardará cada mensaje en la tabla `messages` además de escribir en `mensajes.txt`.
- Si usas Railway: crea un service "Postgres" en tu proyecto y copia la `DATABASE_URL` en las variables del proyecto.


