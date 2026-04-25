from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import random
from telegram import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

TOKEN = "8649811520:AAFJY2fSlk2oJ-9c1jZwNjK6fz37wRtP3f4"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🎮 مرحبا بك في Play & Earn Bot!\nاضغط /spin للعب 🎡")

async def spin(update: Update, context: ContextTypes.DEFAULT_TYPE):
    rewards = ["10 coins", "50 coins", "Try again", "Bonus spin"]
    result = random.choice(rewards)
    await update.message.reply_text(f"🎡 النتيجة: {result}")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("Web App", start))
app.add_handler(CommandHandler("spin", spin))

app.run_polling()
