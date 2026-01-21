import asyncio
from telegram import Bot

TOKEN = "TU API KEY"
CHAT_ID = 4543534534 
RUTA_DOCUMENTO = "documento.pdf"  
MENSAJE = "¡Aquí tienes el documento!"  

async def enviar_documento():
    bot = Bot(token=TOKEN)
    
    # Abrimos el archivo en modo binario
    with open(RUTA_DOCUMENTO, "rb") as doc:
        await bot.send_document(chat_id=CHAT_ID, document=doc, caption=MENSAJE)
    
    print("Documento enviado correctamente ✅")

asyncio.run(enviar_documento())

