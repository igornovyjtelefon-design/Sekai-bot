import os
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Load configuration
TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Welcome to Sekai-bot!')

def help_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Help: Use /info to get info about the bot.')

def info(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Sekai-bot is a demonstration Telegram bot.')

def echo(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(update.message.text)

def stats(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Bot is running smoothly!')

def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher

    # Commands
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('help', help_command))
    dp.add_handler(CommandHandler('info', info))
    dp.add_handler(CommandHandler('echo', echo))
    dp.add_handler(CommandHandler('stats', stats))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()