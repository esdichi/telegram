from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes
import os

TOKEN = "TU API KEY AQUI"
CARPETA_DOCUMENTOS = "documentos_recibidos"
os.makedirs(CARPETA_DOCUMENTOS, exist_ok=True)

async def manejar_documento(update: Update, context: ContextTypes.DEFAULT_TYPE):
    documento = update.message.document  
    file = await documento.get_file()    

    ruta_documento = os.path.join(CARPETA_DOCUMENTOS, documento.file_name)
    await file.download_to_drive(ruta_documento)

    print(f"Documento recibido y guardado en: {ruta_documento}")

    await update.message.reply_text(f"Documento recibido correctamente 📄\nRuta: {ruta_documento}")

app = Application.builder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.Document.ALL, manejar_documento))
app.run_polling()
