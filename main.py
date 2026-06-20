import os
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

BOT_TOKEN = os.getenv("BOT_TOKEN")

QRIS_FILE_ID = "AgACAgUAAxkBAAMJajZKvdsde8SQXr3LSEy0NV0KUewAAnYTaxvJiLlVGK0KlE61LaABAAMCAAN5AAM8BA"

START_TEXT = """
୨ৎ 𓇼 Hello, {name} ♡

Welcome to Disa Apps 🎀⭑.ᐟ

  ୨୧ pricelist ─ /pl
  ୨୧ format order ─ /form
  ୨୧ proof's ─ @disaaproofs

─────୨୧─────

hope you enjoy your stay and happy shopping with us ✦
thank you for choosing
𓇼 Disa Apps⭑.ᐟ 🎀
"""

PL_TEXT = """
✦ — Pricelist Menu ♡

🎀 Premium Apps
୨୧ /streaming ─ Streaming Apps
୨୧ /editing ─ Editing Apps
୨୧ /other ─ Music Apps, AI Tools, dll

──────୨୧──────

🎮 Top Up Games
୨୧ /ff ─ Diamond Free Fire
୨୧ /ml ─ Diamond Mobile Legends

──────୨୧──────

📝 Order Menu
୨୧ /form ─ Format Order

──────୨୧──────

♡ silakan pilih menu yang dibutuhkan
♡ fast response & trusted service
♡ happy shopping at Disa Apps 🎀
"""

FORM_TEXT = """
୨ৎ 📋 Format Order ⭑.ᐟ
<pre>
🎀 All Premium Apps

୨୧ Nama Telegram + Username :
୨୧ Nama Apk :
୨୧ Jenis Apk :
୨୧ Durasi :
୨୧ Payment : 💳 /pay
୨୧ Tag Admin : @disaelyn
</pre>
──────୨୧──────
<pre>
🎀 Top Up Game ML

୨୧ Nama Telegram + Username :
୨୧ Jumlah Diamond :
୨୧ ID Game :
୨୧ Server :
୨୧ Payment : 💳 /pay
୨୧ Tag Admin : @disaelyn
</pre>
──────୨୧──────
<pre>
🎀 Top Up Game FF

୨୧ Nama Telegram + Username :
୨୧ Jumlah Diamond :
୨୧ ID Game :
୨୧ Payment : 💳 /pay
୨୧ Tag Admin : @disaelyn
</pre>
──────୨୧──────

꒰ 📜 ꒱ notes

♡ pastikan data yang dikirim sudah benar
♡ pastikan ID game sudah benar sebelum order
♡ kesalahan data bukan tanggung jawab admin

thank you for shopping at
𓇼 Disa Apps ⭑.ᐟ 🎀
"""

PAY_TEXT = """
୨ৎ Payment QRIS ⭑.ᐟ

♡ silakan melakukan pembayaran melalui QRIS di atas
♡ kirim bukti transfer & sertakan format order ke @disaelyn

──────୨୧──────

୨ৎ 📌 Notes ⭑.ᐟ

♡ mohon membaca ketentuan sebelum melakukan order
♡ order = setuju dengan seluruh ketentuan yang berlaku
♡ no refund setelah pesanan diproses
♡ garansi mengikuti keterangan pada masing-masing produk
♡ keterlambatan respon dapat terjadi di luar jam operasional admin

thank you for shopping at
𓇼 Disa Apps⭑.ᐟ 🎀
"""
STREAMING_TEXT = """
୨ৎ 📺 Streaming Apps ⭑.ᐟ

🎀 Netflix

୨୧ Sharing 1P1U 1 Hari » Rp 5.000
୨୧ Sharing 1P1U 3 Hari » Rp 10.000
୨୧ Sharing 1P1U 7 Hari » Rp 15.000
୨୧ Sharing 1P1U 1 Bulan » Rp 35.000
୨୧ Semi Private 7 Hari » Rp 25.000
୨୧ Semi Private 1 Bulan » Rp 45.000
୨୧ Private 1 Bulan » Rp 170.000
୨୧ Private 1 Bulan (Request Email) » Rp 210.000

──────୨୧──────

🎀 WeTV

୨୧ Sharing 1 Bulan » Rp 10.000
୨୧ Private 1 Bulan » Tanyakan Admin

──────୨୧──────

🎀 Youku

୨୧ Sharing 1 Bulan » Rp 10.000
୨୧ Sharing 3 Bulan » Rp 20.000
୨୧ Private 1 Bulan » Rp 35.000

──────୨୧──────

🎀 Prime Video

୨୧ Sharing 1 Bulan » Rp 10.000
୨୧ Private 1 Bulan » Rp 20.000

──────୨୧──────

🎀 YouTube Premium

୨୧ FamPlan 1 Bulan » Rp 10.000
୨୧ IndiPlan 1 Bulan (B) » Rp 12.000
୨୧ IndiPlan 1 Bulan (S) » Rp 15.000

──────୨୧──────

🎀 Viu

୨୧ Anti Limit 1 Bulan » Rp 1.000
୨୧ Anti Limit 3 Tahun » Rp 5.000

──────୨୧──────

🎀 Bstation

୨୧ Sharing 1 Bulan » Rp 10.000
୨୧ Sharing 3 Bulan » Rp 20.000
୨୧ Private 1 Bulan » Rp 40.000

──────୨୧──────

🎀 IQIYI

୨୧ Standar 1 Bulan » Rp 10.000
୨୧ Standar Private 1 Bulan » Rp 25.000
୨୧ Premium 1 Bulan » Rp 15.000

──────୨୧──────

🎀 LokLok

୨୧ Sharing Basic 1 Bulan » Rp 20.000
୨୧ Sharing Standar 1 Bulan » Rp 25.000

──────୨୧──────

🎀 Vidio

୨୧ Sharing Mobile 1 Bulan » Rp 25.000
୨୧ Private Mobile 1 Bulan » Rp 35.000

──────୨୧──────

꒰ 📜 ꒱ notes

♡ harga dapat berubah sewaktu-waktu
♡ mohon tanyakan stok sebelum order
♡ garansi sesuai masa aktif produk

thank you for shopping at
𓇼 Disa Apps ⭑.ᐟ 🎀
"""

EDITING_TEXT = """
୨ৎ 🎨 Editing Apps ⭑.ᐟ

🎀 Canva

୨୧ Member 1 Hari » Rp 500
୨୧ Member 7 Hari » Rp 1.000
୨୧ Member 1 Bulan » Rp 2.000
୨୧ Head 1 Bulan » Rp 10.000
୨୧ Education Lifetime » Rp 15.000

──────୨୧──────

🎀 CapCut

୨୧ Sharing 7 Hari » Rp 5.000
୨୧ Sharing 1 Bulan » Rp 10.000
୨୧ Private 7 Hari » Rp 7.000
୨୧ Private 1 Bulan » Rp 15.000

──────୨୧──────

🎀 PicsArt

୨୧ Sharing 1 Bulan » Rp 10.000
୨୧ Private 1 Bulan » Rp 15.000

──────୨୧──────

🎀 Meitu

୨୧ Private 7 Hari (Android) » Rp 10.000

──────୨୧──────

🎀 Wink

୨୧ Private 7 Hari (Android) » Rp 10.000

──────୨୧──────

🎀 Alight Motion

୨୧ Private 1 Year » Rp 5.000
୨୧ Private 1 Year (iOS) » Rp 10.000

──────୨୧──────

꒰ 📜 ꒱ notes

♡ harga dapat berubah sewaktu-waktu
♡ mohon tanyakan stok sebelum order
♡ garansi sesuai masa aktif produk

thank you for shopping at
𓇼 Disa Apps ⭑.ᐟ 🎀
"""
OTHER_TEXT = """
୨ৎ 🤍 Other Apps ⭑.ᐟ

🎀 Spotify Premium

୨୧ FamPlan 1 Bulan » Rp 25.000
୨୧ IndiPlan 1 Bulan » Rp 30.000

──────୨୧──────

🎀 Apple Music

୨୧ iMess 1 Bulan » Rp 10.000

──────୨୧──────

🎀 ChatGPT Plus

୨୧ Sharing 1 Bulan (NoGar) » Rp 10.000
୨୧ Sharing 1 Bulan (FullGar) » Rp 20.000

──────୨୧──────

🎀 Gemini AI

୨୧ Via Invite 1 Bulan » Rp 12.000
୨୧ Via Invite 2 Bulan » Rp 18.000
୨୧ Via Invite 3 Bulan » Rp 25.000
୨୧ Via Invite 4 Bulan » Rp 30.000

──────୨୧──────

🎀 GetContact

୨୧ Premium 1 Bulan » Rp 15.000
୨୧ Cek Nomor GTC » Rp 10.000

──────୨୧──────

🎀 Grok AI

୨୧ 7 Hari Private » Rp 15.000
୨୧ 14 Hari Private » Rp 25.000

──────୨୧──────

꒰ 📜 ꒱ notes

♡ harga dapat berubah sewaktu-waktu
♡ mohon tanyakan stok sebelum order
♡ garansi sesuai masa aktif produk

thank you for shopping at
𓇼 Disa Apps ⭑.ᐟ 🎀
"""

FF_TEXT = """
୨ৎ 🎮 Free Fire Topup ⭑.ᐟ

🎀 Diamond List

୨୧ 5 DM » Rp 2.500
୨୧ 10 DM » Rp 3.500
୨୧ 12 DM » Rp 4.000
୨୧ 20 DM » Rp 6.000
୨୧ 30 DM » Rp 8.000
୨୧ 50 DM » Rp 10.500
୨୧ 80 DM » Rp 15.000
୨୧ 100 DM » Rp 19.000
୨୧ 120 DM » Rp 21.500
୨୧ 140 DM » Rp 25.500
୨୧ 160 DM » Rp 28.000
୨୧ 400 DM » Rp 65.000

──────୨୧──────

꒰ 📜 ꒱ notes

♡ proses menggunakan ID game
♡ mohon tanyakan stok sebelum order
♡ produk yang tidak ada di list bisa ditanyakan ke admin

thank you for shopping at
𓇼 Disa Apps ⭑.ᐟ 🎀
"""

ML_TEXT = """
୨ৎ 🎮 Mobile Legends Topup ⭑.ᐟ

🎀 Diamond List

୨୧ 5 DM » Rp 2.500
୨୧ 10 DM » Rp 3.500
୨୧ 12 DM » Rp 4.000
୨୧ 20 DM » Rp 6.000
୨୧ 25 DM » Rp 6.500
୨୧ 30 DM » Rp 7.500
୨୧ 50 DM » Rp 10.000
୨୧ 55 DM » Rp 10.500
୨୧ 70 DM » Rp 12.500
୨୧ 75 DM » Rp 13.500
୨୧ 80 DM » Rp 14.500
୨୧ 90 DM » Rp 16.000

──────୨୧──────

꒰ 📜 ꒱ notes

♡ proses menggunakan ID game & server
♡ mohon tanyakan stok sebelum order
♡ produk yang tidak ada di list bisa ditanyakan ke admin

thank you for shopping at
𓇼 Disa Apps ⭑.ᐟ 🎀
"""
# =========================
# HANDLER
# =========================

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    name = update.effective_user.first_name

    await update.message.reply_text(
        START_TEXT.format(name=name)
    )

async def pl(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(PL_TEXT)

async def form(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        FORM_TEXT,
        parse_mode="HTML"
    )

async def pay(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_photo(
        photo=QRIS_FILE_ID,
        caption=PAY_TEXT
    )

async def streaming(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(STREAMING_TEXT)

async def editing(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(EDITING_TEXT)

async def other(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(OTHER_TEXT)

async def ff(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(FF_TEXT)

async def ml(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(ML_TEXT)

# =========================
# AUTO WELCOME MEMBER BARU
# =========================

async def welcome_member(update: Update, context: ContextTypes.DEFAULT_TYPE):
    for member in update.message.new_chat_members:
        await update.message.reply_text(
            START_TEXT.format(name=member.first_name)
        )

# =========================
# UNKNOWN COMMAND
# =========================

async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        """
୨ৎ command tidak ditemukan ♡

silakan gunakan:
୨୧ /pl
୨୧ /form

thank you for choosing
𓇼 Disa Apps ⭑.ᐟ 🎀
"""
    )

# =========================
# APP
# =========================

app = ApplicationBuilder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("pl", pl))
app.add_handler(CommandHandler("form", form))
app.add_handler(CommandHandler("pay", pay))
app.add_handler(CommandHandler("streaming", streaming))
app.add_handler(CommandHandler("editing", editing))
app.add_handler(CommandHandler("other", other))
app.add_handler(CommandHandler("ff", ff))
app.add_handler(CommandHandler("ml", ml))

app.add_handler(
    MessageHandler(
        filters.StatusUpdate.NEW_CHAT_MEMBERS,
        welcome_member
    )
)

app.add_handler(
    MessageHandler(filters.COMMAND, unknown)
)

if __name__ == "__main__":
    app.run_polling()
