from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "TU API KEY"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Hola!\n")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.args[0]
    context.args[1]
    context.args[2]


app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("hola", start))
app.add_handler(CommandHandler("repite", echo))

app.run_polling()

