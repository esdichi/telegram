import subprocess
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "TU API KEY"

async def apagar(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Confirmado. Apagando el sistema... ⚡")
    
    subprocess.run(["shutdown", "/s", "/t", "1"])

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("apagar", apagar))
app.run_polling()

