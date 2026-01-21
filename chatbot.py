from google import genai
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes

GENAI_API_KEY = "API KEY DE GOOGLE"
TELEGRAM_TOKEN = "API KEY DE TELEGRAM"
client = genai.Client(api_key=GENAI_API_KEY)
chat = client.chats.create(model="gemini-2.5-flash")

async def manejar_mensaje(update: Update, context: ContextTypes.DEFAULT_TYPE):
    texto = update.message.text
    print(f"Mensaje recibido: {texto}")

    try:
        respuesta = chat.send_message(texto)
        await update.message.reply_text(respuesta.text)
    except Exception as e:
        await update.message.reply_text(f"Error al procesar el mensaje: {e}")
        print(f"Error: {e}")

app = Application.builder().token(TELEGRAM_TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, manejar_mensaje))

print("Bot de Telegram iniciado...")
app.run_polling()

    