from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes
import os

TOKEN = "TU TOKEN"
CARPETA_VIDEOS = "videos_recibidos"
os.makedirs(CARPETA_VIDEOS, exist_ok=True)

async def manejar_video(update: Update, context: ContextTypes.DEFAULT_TYPE):
    video = update.message.video  
    file = await video.get_file() 

    ruta_video = os.path.join(CARPETA_VIDEOS, f"{video.file_id}.mp4")
    await file.download_to_drive(ruta_video)

    print(f"Video recibido y guardado en: {ruta_video}")

    await update.message.reply_text(f"Video recibido correctamente 🎬\nRuta: {ruta_video}")

app = Application.builder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.VIDEO, manejar_video))
app.run_polling()