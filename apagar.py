import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TELEGRAM_TOKEN = "TU TOKEN_AQUI"

USUARIOS_AUTORIZADOS = [12321321312] 

async def apagar_pc(update: Update, context: ContextTypes.DEFAULT_TYPE):
    usuario_id = update.effective_user.id
    if usuario_id not in USUARIOS_AUTORIZADOS:
        await update.message.reply_text("No estás autorizado para apagar el PC.")
        return

    await update.message.reply_text("Apagando el PC en 10 segundos...")
    print("Comando de apagado recibido desde Telegram.")
    
    os.system("notepad")  # /s = apagar, /t 10 = en 10 segundos


app = Application.builder().token(TELEGRAM_TOKEN).build()

app.add_handler(CommandHandler("apagar", apagar_pc))

print("Bot de Telegram iniciado...")
app.run_polling()
