import asyncio
from telegram import Bot

TOKEN = "tu api key"
CHAT_ID = 54654645654 
RUTA_VIDEO = "video.mp4"
MENSAJE = "¡Aquí tienes el video!"  

async def enviar_video():
    bot = Bot(token=TOKEN)
    
    with open(RUTA_VIDEO, "rb") as video:
        await bot.send_video(chat_id=CHAT_ID, video=video, caption=MENSAJE)
    
    print("Video enviado correctamente ✅")

asyncio.run(enviar_video())


