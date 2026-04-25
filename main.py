from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackQueryHandler
import random

# 🔑 حط التوكن هنا
TOKEN = "8649811520:AAFJY2fSlk2oJ-9c1jZwNjK6fz37wRtP3f4"

# 👤 تخزين المستخدمين (مؤقت)
users = {}

def get_user(user_id):
    if user_id not in users:
        users[user_id] = {
            "vip": 0,
            "spins": 3,
            "coins": 0
        }
    return users[user_id]

# 🚀 start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = get_user(update.effective_user.id)

    keyboard = [
        [InlineKeyboardButton("🎡 Spin", callback_data="spin")],
        [InlineKeyboardButton("💎 VIP", callback_data="vip")]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "🎮 مرحبا بك في Play & Earn Bot!\n"
        f"💰 Coins: {user['coins']}\n"
        f"🎟 Spins: {user['spins']}\n"
        f"👑 VIP: {user['vip']}",
        reply_markup=reply_markup
    )

# 🎯 handler للأزرار
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    user = get_user(query.from_user.id)

    if query.data == "spin":

        if user["vip"] == 0 and user["spins"] <= 0:
            await query.edit_message_text(
                "❌ انتهت spins المجانية!\n"
                "💎 VIP1 بـ 10$ USDT"
            )
            return

        if user["vip"] == 0:
            user["spins"] -= 1

        rewards = [
            ("10 coins", 50),
            ("20 coins", 30),
            ("50 coins", 15),
            ("100 coins", 5)
        ]

        result = random.choice(rewards)
        coins_won = int(result[0].split()[0])
        user["coins"] += coins_won

        keyboard = [
            [InlineKeyboardButton("🎡 Spin مرة أخرى", callback_data="spin")],
            [InlineKeyboardButton("💎 VIP", callback_data="vip")]
        ]

        reply_markup = InlineKeyboardMarkup(keyboard)

        await query.edit_message_text(
            f"🎡 النتيجة: {result[0]}\n"
            f"💰 مجموعك: {user['coins']} coins\n"
            f"🎟 باقي spins: {user['spins']}",
            reply_markup=reply_markup
        )

    elif query.data == "vip":
        await query.edit_message_text(
            "💎 VIP1 = 10$ USDT\n"
            "📩 تواصل مع الأدمن للتفعيل"
        )

# ▶️ تشغيل البوت
app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button_handler))

app.run_polling()
        
