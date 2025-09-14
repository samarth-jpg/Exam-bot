import os
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Get your bot token from Render Environment Variable
BOT_TOKEN = os.environ.get("BOT_TOKEN")

# /start command
def start(update: Update, context: CallbackContext):
    update.message.reply_text(
        "👋 Welcome to Exam Bot!\n\n"
        "Use /papers to get previous year exam question papers 📄."
    )

# /papers command
def papers(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Here are some sample exam papers:\n\n"
        "1️⃣ SSC 2022 - https://example.com/ssc2022.pdf\n"
        "2️⃣ UPSC 2021 - https://example.com/upsc2021.pdf\n"
        "3️⃣ Banking 2020 - https://example.com/bank2020.pdf\n"
    )

def main():
    if not BOT_TOKEN:
        print("❌ ERROR: BOT_TOKEN is not set. Please add it in Render Environment Variables.")
        return

    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    # Register commands
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("papers", papers))

    # Start bot
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
