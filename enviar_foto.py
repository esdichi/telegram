import asyncio
from telegram import Bot

TOKEN = "TU API KEY"
CHAT_ID = 45435435345
RUTA_FOTO = "imagen.jpg" 
MENSAJE = "¡Aquí está la foto que quería enviarte!"  

async def enviar_foto():
    bot = Bot(token=TOKEN)
    
    with open(RUTA_FOTO, "rb") as foto:
        await bot.send_photo(chat_id=CHAT_ID, photo=foto, caption=MENSAJE)
    
    print("Foto enviada correctamente ✅")

asyncio.run(enviar_foto())

