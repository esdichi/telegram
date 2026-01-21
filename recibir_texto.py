from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes

TOKEN = "TU API KEY"

async def manejar_mensaje(update: Update, context: ContextTypes.DEFAULT_TYPE):
    texto = update.message.text

    print(f"Mensaje recibido: {texto}")

    await update.message.reply_text(f"Recibido tu mensaje: {texto}")


app = Application.builder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.ALL, manejar_mensaje))
app.run_polling()


