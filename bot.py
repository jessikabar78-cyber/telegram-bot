from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
import requests

BOT_TOKEN = "7576261047:AAHXxkGR_GlRsGnWQMXhjeUrdPF3uRV_eMs"
API_KEY = "2557b2347e834f550b1ffe5967f9d2ee"
API_URL = "https://smmapi.net/api/v2"
SERVICE_ID = "8729"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("ارسل الرابط وعدد المتابعين مثل:\nlink 100")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = update.message.text.split()

    if len(text) != 2:
        await update.message.reply_text("اكتب الرابط وعدد المتابعين فقط")
        return

    link = text[0]
    quantity = text[1]

    data = {
        "key": API_KEY,
        "action": "add",
        "service": SERVICE_ID,
        "link": link,
        "quantity": quantity
    }

    requests.post(API_URL, data=data)

    await update.message.reply_text("تم ارسال الطلب بنجاح")

app = ApplicationBuilder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT, handle_message))

app.run_polling()
