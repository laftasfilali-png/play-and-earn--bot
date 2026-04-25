from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import random

# 🔑 ضع التوكن هنا من BotFather
TOKEN = "8649811520:AAFJY2fSlk2oJ-9c1jZwNjK6fz37wRtP3f4"

# 👤 تخزين بسيط للمستخدمين (MVP)
users = {}

def get_user(user_id):
    if user_id not in users:
        users[user_id] = {
            "vip": 0,
            "spins": 3,
            "coins": 0
        }
    return users[user_id]

# 🚀 start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = get_user(update.effective_user.id)

    await update.message.reply_text(
        "🎮 مرحبا بك في Play & Earn Bot!\n"
        "🎡 استعمل /spin للعب\n"
        f"💰 Coins: {user['coins']}\n"
        f"🎟 Spins: {user['spins']}\n"
        f"👑 VIP: {user['vip']}"
    )

# 🎡 spin command
async def spin(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = get_user(update.effective_user.id)

    # 🔒 check VIP or spins
    if user["vip"] == 0 and user["spins"] <= 0:
        await update.message.reply_text(
            "❌ انتهت spins المجانية!\n"
            "💎 اشترك في VIP1 بـ 10$ USDT لمواصلة اللعب"
        )
        return

    if user["vip"] == 0:
        user["spins"] -= 1

    # 🎁 rewards
    rewards = [
        ("10 coins", 50),
        ("20 coins", 30),
        ("50 coins", 15),
        ("100 coins", 5)
    ]

    result = random.choice(rewards)
    coins_won = int(result[0].split()[0])

    user["coins"] += coins_won

    await update.message.reply_text(
        f"🎡 النتيجة: {result[0]}\n"
        f"💰 مجموعك: {user['coins']} coins\n"
        f"🎟 باقي spins: {user['spins']}"
    )

# ▶️ تشغيل البوت
app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("spin", spin))

app.run_polling()
