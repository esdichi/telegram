from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes

TOKEN = "TU TOKEN AQUI"

async def recibir_mensaje(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id

    print(f"Chat ID: {chat_id}")
    await update.message.reply_text(f"Tu chat ID es: {chat_id}")

app = Application.builder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.ALL, recibir_mensaje))
    
app.run_polling()

