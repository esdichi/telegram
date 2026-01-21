import asyncio
from telegram import Bot

TOKEN = "TU TOKEN"
CHAT_ID = 3432432432  

async def enviar_mensaje():
    bot = Bot(token=TOKEN)
    await bot.send_message(chat_id=CHAT_ID, text="¡Hola! Este es un mensaje directo sin polling 🚀")
    print("Mensaje enviado correctamente ✅")

asyncio.run(enviar_mensaje())


