import os
import telebot

# Get your bot token from environment variable
BOT_TOKEN = os.environ.get("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)

# Example command
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "👋 Hello! Your bot is live and working!")

# Example echo handler
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

print("🤖 Bot is running...")
bot.infinity_polling()