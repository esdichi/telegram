from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes
import os

TOKEN = "TU TOKEN"
CARPETA_AUDIOS = "audios_recibidos"
CARPETA_VOICES = "notas_voz"
os.makedirs(CARPETA_AUDIOS, exist_ok=True)
os.makedirs(CARPETA_VOICES, exist_ok=True)

async def manejar_audio(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.audio:
        audio = update.message.audio
        file = await audio.get_file()
        ruta_audio = os.path.join(CARPETA_AUDIOS, f"{audio.file_id}.mp3")
        await file.download_to_drive(ruta_audio)
    elif update.message.voice:
        voice = update.message.voice
        file = await voice.get_file()
        ruta_voice = os.path.join(CARPETA_VOICES, f"{voice.file_id}.ogg")
        await file.download_to_drive(ruta_voice)

app = Application.builder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.AUDIO | filters.VOICE, manejar_audio))
app.run_polling()
