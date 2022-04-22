
import logging
import requests
from requests import Session
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import InputMediaPhoto

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


#Command Handlers
def start(update, context):
    update.message.reply_text('BOT ACTIVATED')


#function to respond to help cmd
def help(update, context):
    update.message.reply_text('I can not help you yet, sorry.')

#function to echo the users message
def echo(update, context):
    update.message.reply_text(update.message.text + '' + ' is not a command I know.')

#function to log errors and display
def error(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)

#command to send a cute cat picture






def main():
    updater = Updater("5185398555:AAFQyiI65gVixhpuy1QVyAykA29XFiPUJvc", use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
   
    dp.add_handler(MessageHandler(Filters.text, echo))
    dp.add_error_handler(error)
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()