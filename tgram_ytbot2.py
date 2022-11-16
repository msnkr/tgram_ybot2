from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
import logging
from dotenv import load_dotenv
import os

load_dotenv('.env')
files_end = ['.mp4', '.mp3', '.webm', '.part']
def clear_downloads():


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='Enter URL: ')


def help(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='Takes long to download: The Youtube-dl api seems to be capped at 50Kpbs. Unfortunately there isn\'t much I can do about this. The original maintainer of the repo would have to fix this. I might try bypass youtube-dl but that is for a future release. ')



def main():
    updater = Updater(token=os.getenv('TOKEN'))
    dispatcher = updater.dispatcher
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)

    updater.dispatcher.add_handler(CommandHandler('help', help))
    


    updater.start_polling()
    updater.idle()

main()