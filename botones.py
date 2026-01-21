from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (Application,CommandHandler,CallbackQueryHandler,ContextTypes)

TOKEN = "TU TOKEN"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [
            InlineKeyboardButton("📸 Foto", callback_data="foto"),
            InlineKeyboardButton("🎬 Video", callback_data="video")
        ],
        [
            InlineKeyboardButton("ℹ️ Info", callback_data="info")
        ]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "Elige una opción:",
        reply_markup=reply_markup
    )


async def botones(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "foto":
        await query.message.reply_text("Has pulsado 📸 Foto")

    elif query.data == "video":
        await query.message.reply_text("Has pulsado 🎬 Video")

    elif query.data == "info":
        await query.message.reply_text("Este es un bot de ejemplo con botones")


app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(botones))
app.run_polling()


