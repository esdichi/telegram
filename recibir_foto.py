from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes
import os

TOKEN = "TU API KEY"
CARPETA_FOTOS = "imagenes_recibidas"
os.makedirs(CARPETA_FOTOS, exist_ok=True)

async def manejar_foto(update: Update, context: ContextTypes.DEFAULT_TYPE):
    photo = update.message.photo[-1]  
    file = await photo.get_file()     

    ruta_foto = os.path.join(CARPETA_FOTOS, f"{photo.file_id}.jpg")
    await file.download_to_drive(ruta_foto)

    print(f"Foto recibida y guardada en: {ruta_foto}")

    await update.message.reply_text(f"Foto recibida correctamente 📸\nRuta: {ruta_foto}")

app = Application.builder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.PHOTO, manejar_foto))
app.run_polling()
