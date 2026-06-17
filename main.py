import os
from telegram import (
    Update,
    ReplyKeyboardMarkup,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)
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

STREAMING_TEXT = """
→ APLIKASI STREAMING

⠀⠀ᝰ.ᐟ Netflix
⤿ sharing 1u 1d :: Rp 5.000
⤿ sharing 1u 3d :: Rp 10.000
⤿ sharing 1u 7d :: Rp 15.000
⤿ sharing 1u 1b :: Rp 35.000
⤿ semi priv 7d :: Rp 25.000
⤿ semi priv 1b :: Rp 45.000
⤿ private 1b :: Rp 170.000
⤿ private 1b :: Rp 210.000 (req email bisa dari mu)

⠀⠀ᝰ.ᐟ WeTV
⤿ sharing 1 bulan :: Rp 10.000
⤿ private 1 bulan :: tanyakan

⠀⠀ᝰ.ᐟ Youku
⤿ sharing 1 bulan :: Rp 10.000
⤿ sharing 3 bulan :: Rp 20.000
⤿ private 1 bulan :: Rp 35.000

⠀⠀ᝰ.ᐟ Prime Video
⤿ sharing 1 bulan :: Rp 10.000
⤿ private 1 bulan :: Rp 20.000

⠀⠀ᝰ.ᐟ YouTube
⤿ famplan 1 bulan :: Rp 10.000
⤿ indiplan 1 bulan (b) :: Rp 12.000
⤿ indiplan 1 bulan (s) :: Rp 15.000

⠀⠀ᝰ.ᐟ Viu
⤿ anti limit 1 bulan :: Rp 1.000
⤿ anti limit 3 tahun :: Rp 5.000

⠀⠀ᝰ.ᐟ Bstation
⤿ sharing 1 bulan :: Rp 10.000
⤿ sharing 3 bulan :: Rp 20.000
⤿ private 1 bulan :: Rp 40.000

⠀⠀ᝰ.ᐟ IQIYI
⤿ standar 1 bulan :: Rp 10.000
⤿ standar priv 1 bulan :: Rp 25.000
⤿ premium 1 bulan :: Rp 15.000

⠀⠀ᝰ.ᐟ LokLok
⤿ sharing basic 1 bulan :: Rp 20.000
⤿ sharing standar 1 bulan :: Rp 25.000

⠀⠀ᝰ.ᐟ Vidio
⤿ sharing mobile 1 bulan :: Rp 25.000
⤿ private mobile 1 bulan :: Rp 35.000
"""

EDITING_TEXT = """
→ APK EDITING

⠀⠀ᝰ.ᐟ Canva
⤿ member 1 hari :: Rp 500
⤿ member 7 hari :: Rp 1.000
⤿ member 1 bulan :: Rp 2.000
⤿ head 1 bulan :: Rp 10.000
⤿ education lifetime :: Rp 15.000

⠀⠀ᝰ.ᐟ CapCut
⤿ sharing 7 hari :: Rp 5.000
⤿ sharing 1 bulan :: Rp 10.000
⤿ private 7 hari :: Rp 7.000
⤿ private 1 bulan :: Rp 15.000

⠀⠀ᝰ.ᐟ PicsArt
⤿ sharing 1 bulan :: Rp 10.000
⤿ private 1 bulan :: Rp 15.000

⠀⠀ᝰ.ᐟ Meitu
⤿ private 7 hari andro :: Rp 10.000

⠀⠀ᝰ.ᐟ Wink
⤿ private 7 hari andro :: Rp 10.000

⠀⠀ᝰ.ᐟ Alight Motion
⤿ private 1 year :: Rp 5.000
⤿ private 1 year IOS :: Rp 10.000
"""

MUSIC_TEXT = """
→ MUSIC NEED'S ⭑.ᐟ

⠀⠀ᝰ.ᐟ Spotify
⤿ famplan 1 bulan :: Rp 25.000
⤿ indiplan 1 bulan :: Rp 30.000

⠀⠀ᝰ.ᐟ Apple Music
⤿ imess 1 bulan :: Rp 10.000

⠀⠀ᝰ.ᐟ ChatGPT
⤿ sharing 1 bulan nogar :: Rp 10.000
⤿ sharing 1 bulan fullgar :: Rp 20.000

⠀⠀ᝰ.ᐟ Gemini AI
⤿ via Invite 1b :: Rp 12.000
⤿ via Invite 2b :: Rp 18.000
⤿ via Invite 3b :: Rp 25.000
⤿ via Invite 4b :: Rp 30.000

⠀⠀ᝰ.ᐟ Get Contact
⤿ Premium 1b :: Rp 15.000
⤿ Cek Nomor GTC :: Rp 10.000

⠀⠀ᝰ.ᐟ Grok AI
⤿ 7 Hari Private :: Rp 15.000
⤿ 14 Hari Private :: Rp 25.000
"""

INFO_TEXT = """
📑 inform's

• kode b = bulan
• kode d = day (hari)
• kode y/t = tahun
• harga dapat berubah sewaktu-waktu
• harap tanyakan stok sebelum order
• fast respon & fast proses
• garansi sesuai masa aktif
• order = setuju dengan syarat & ketentuan
• yang tidak ada di list bisa tanyakan admin

━━━━━━━━━━━━━━
୨ৎ Trusted Premium Seller
୨ৎ Fast Response & Process
୨ৎ Bergaransi Sesuai Ketentuan
୨ৎ Open Reseller & Dropship
━━━━━━━━━━━━━━
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


async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "✦ Streaming":
        await update.message.reply_text(STREAMING_TEXT)

    elif text == "✦ Editing":
        await update.message.reply_text(EDITING_TEXT)

    elif text == "✦ Music & AI":
        await update.message.reply_text(MUSIC_TEXT)

    elif text == "✦ Informasi":
        await update.message.reply_text(INFO_TEXT)

    elif text == "✦ Order":
        keyboard = [
            [
                InlineKeyboardButton(
                    "✦ Chat Admin",
                    url="https://t.me/disaelyn"
                )
            ]
        ]

        reply_markup = InlineKeyboardMarkup(keyboard)

        await update.message.reply_text(
            """
୨ৎ Ready to Order?

Format Order:
⤿ Produk:
⤿ Durasi:
⤿ Email:
⤿ Pembayaran:

Klik tombol di bawah untuk menghubungi admin.
            """,
            reply_markup=reply_markup
        )


app = ApplicationBuilder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))

app.add_handler(
    MessageHandler(
        filters.TEXT & ~filters.COMMAND,
        button_handler
    )
)

if __name__ == "__main__":
    app.run_polling(
        allowed_updates=Update.ALL_TYPES
        )
