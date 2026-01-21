import asyncio
from telegram import Bot

TOKEN = "TU API KEY"
CHAT_ID = 54543543534534
RUTA_AUDIO = "audio.mp3"  
MENSAJE = "¡Aquí tienes el audio!" 

async def enviar_audio():
    bot = Bot(token=TOKEN)

    with open(RUTA_AUDIO, "rb") as audio:
        await bot.send_audio(chat_id=CHAT_ID, audio=audio, caption=MENSAJE)
    
    print("Audio enviado correctamente ✅")

asyncio.run(enviar_audio())

