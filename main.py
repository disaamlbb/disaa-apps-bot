import os
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

BOT_TOKEN = os.getenv("BOT_TOKEN")

START_TEXT = """
୨ৎ Welcome to Disaa Apps Store

Halo! Selamat datang di Disaa Apps ⭑.ᐟ
Trusted Premium Seller dengan proses cepat & aman.

╭─ ✦ MENU ✦ ─╮
⌞ Streaming
⌞ Editing
⌞ Music & AI
⌞ Informasi
⌞ Order
╰──────────╯

── ⋆⋅☆⋅⋆ ──

୨ৎ Trusted Premium Seller
୨ৎ Fast Response & Process
୨ৎ Bergaransi Sesuai Ketentuan
୨ৎ Open Reseller & Dropship
"""

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        ["✦ Streaming", "✦ Editing"],
        ["✦ Music & AI", "✦ Informasi"],
        ["✦ Order"],
    ]

    reply_markup = ReplyKeyboardMarkup(
        keyboard,
        resize_keyboard=True
    )

    await update.message.reply_text(
        START_TEXT,
        reply_markup=reply_markup
    )

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))

app.run_polling()
