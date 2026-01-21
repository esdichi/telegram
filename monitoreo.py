
import psutil
import asyncio
from telegram import Bot


TOKEN = "TU_TOKEN"  # Pon aquí tu token de Telegram
CHAT_ID = 3432432432  # Tu chat ID
UMBRAL_CPU = 80  # Porcentaje de CPU que dispara la alerta
INTERVALO = 5  # Cada cuantos segundos revisamos la CPU

# --- Función para enviar mensajes ---
async def enviar_mensaje(texto):
    bot = Bot(token=TOKEN)
    await bot.send_message(chat_id=CHAT_ID, text=texto)
    print("Mensaje enviado:", texto)

# --- Función principal de monitorización ---
async def monitorizar_cpu():
    alerta_enviada = False  # Para no enviar spam continuo
    while True:
        cpu = psutil.cpu_percent(interval=1, percpu=True)
        promedio_cpu = sum(cpu)/len(cpu)
        print(f"CPU promedio: {promedio_cpu:.1f}%")

        if promedio_cpu > UMBRAL_CPU and not alerta_enviada:
            await enviar_mensaje(f"⚠️ Alerta de CPU: {promedio_cpu:.1f}%")
            alerta_enviada = True  # Bloquea nuevas alertas hasta que baje
        elif promedio_cpu <= UMBRAL_CPU:
            alerta_enviada = False  # Restablece la alerta

        await asyncio.sleep(INTERVALO)

# --- Ejecutar ---
asyncio.run(monitorizar_cpu())
