import os
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# 🔐 TOKEN from Render environment variables
TOKEN = os.getenv("TOKEN")

if not TOKEN:
    raise Exception("TOKEN not set in environment variables")

# 📱 MENU
keyboard = ReplyKeyboardMarkup(
    [["🛒 Buy ATABS", "🛒 Buy PINAY"], ["📤 Send Receipt"]],
    resize_keyboard=True
)

# 🚀 START COMMAND
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🔥 ATABS PINAY VIP 🔥\n\n"
        "📦 PRICES:\n"
        "• 💎 ATABS - 250 pesos\n"
        "• 🌸 PINAY - 150 pesos\n\n"
        "♾️ LIFETIME ACCESS\n\n"
        "💸 GCash: 09763185206\n"
        "👤 Name: G***** G*******\n\n"
        "📩 Send receipt to confirm payment\n",
        reply_markup=keyboard
    )

# 🎯 TEXT HANDLER
async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "🛒 Buy ATABS":
        await update.message.reply_text("💎 ATABS - 250 pesos\nSend GCash payment")

    elif text == "🛒 Buy PINAY":
        await update.message.reply_text("🌸 PINAY - 150 pesos\nSend GCash payment")

    elif text == "📤 Send Receipt":
        await update.message.reply_text("📩 Send receipt here 👉 @S3ndh3re")

    else:
        await update.message.reply_text("Use the buttons below 👇")

# 📸 PHOTO HANDLER
async def handle_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Receipt received!")

# ▶️ MAIN FUNCTION
def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text))
    app.add_handler(MessageHandler(filters.PHOTO, handle_photo))

    print("🚀 Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
