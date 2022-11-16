from __future__ import unicode_literals
from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
import logging
from dotenv import load_dotenv
import os
import youtube_dl


load_dotenv('.env')
files_end = ['.mp4', '.mp3', '.webm', '.part']

def clear_downloads():
    for file in os.listdir(r'C:\Users\Digital\Documents\GitHub\tgram_ybot2'):
        for item in files_end:
            if file.endswith(item):
                os.remove(file)
        

def download(update: Update, context: CallbackContext):
    clear_downloads()
    text = update.message.text.split(" ")
    with youtube_dl.YoutubeDL({'format': '18'}) as ydl:
        ydl.download([text[1]])
    update.message.reply_text(text)


def help(update, context):
    update.message.reply_text('Takes long to download: The Youtube-dl api seems to be capped at 50Kpbs. Unfortunately there isn\'t much I can do about this. The original maintainer of the repo would have to fix this. I might try bypass youtube-dl but that is for a future release. ')


def start(update, context):
    update.message.reply_text('Welcome to url Youtube Downloader')


def main():
    updater = Updater(token=os.getenv('TOKEN'))
    dispatcher = updater.dispatcher
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CommandHandler('help', help))
    updater.dispatcher.add_handler(CommandHandler('download', download))
    
    updater.start_polling()
    updater.idle()

main()