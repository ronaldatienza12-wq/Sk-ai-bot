import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = os.getenv("8566458521:AAG3pZVCOHnyF0Pv2PQiRWA19P2dJDqv9AQ")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! 🤖 Ako ang SK AI Assistant. Paano kita matutulungan?")

async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()

    if "schedule" in text:
        await update.message.reply_text("📅 Next SK Session: Sunday, 2PM.")
    elif "project" in text:
        await update.message.reply_text("📢 Current Project: Youth Tutoring Program.")
    else:
        await update.message.reply_text("Salamat sa message! Ire-review ng SK team.")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply))

app.run_polling()
