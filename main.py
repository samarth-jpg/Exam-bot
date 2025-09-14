import os
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Get your bot token from BotFather and put it here
BOT_TOKEN = os.environ.get("BOT_TOKEN", 8309253554:AAEoz-047cDy-ORRUfMv_BCzscPqA2eEqDE
)

# 📌 Start command
def start(update: Update, context: CallbackContext):
    update.message.reply_text(
        "👋 Welcome to Exam Bot!\n\n"
        "Use /papers to get previous year exam question papers 📄."
    )

# 📌 Papers command
def papers(update: Update, context: CallbackContext):
    # Later, you can fetch from Google Drive / Database
    update.message.reply_text(
        "Here are some sample exam papers:\n\n"
        "1️⃣ SSC 2022 - https://example.com/ssc2022.pdf\n"
        "2️⃣ UPSC 2021 - https://example.com/upsc2021.pdf\n"
        "3️⃣ Banking 2020 - https://example.com/bank2020.pdf\n"
    )

def main():
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    # Commands
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("papers", papers))

    # Start bot
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
