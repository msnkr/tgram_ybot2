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
files_end = ['.mp4', '.mp3', '.webm', '.part', '.mkv']

def download_video(update: Update, context: CallbackContext):
    for file in os.listdir(r'C:\Users\Digital\Documents\GitHub\tgram_ybot2'):
        for item in files_end:
            if file.endswith(item):
                context.bot.send_video(chat_id=update.effective_chat.id, video=open(f'{file}', 'rb'))
                clear_downloads()


def download(update: Update, context: CallbackContext):
    clear_downloads()
    text = update.message.text.split(" ")
    video_text = text[1]
    update.message.reply_text('Downloading Video now. Please wait..')
    with youtube_dl.YoutubeDL({'format': '22'}) as ydl:
       ydl.download([video_text])
    update.message.reply_text('Your video has finished downloading. Send {/dv} to download your video. ')


def clear_downloads():
    for file in os.listdir(r'C:\Users\Digital\Documents\GitHub\tgram_ybot2'):
        for item in files_end:
            if file.endswith(item):
                os.remove(file)
        

def help(update, context):
    update.message.reply_text('Takes long to download: Look like Google doesn\'t like downloading higher than 50Kbps.')

def start(update, context):
    update.message.reply_text('Welcome to url Youtube Downloader')


def main():
    updater = Updater(token=os.getenv('TOKEN'))
    dispatcher = updater.dispatcher
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CommandHandler('help', help))
    updater.dispatcher.add_handler(CommandHandler('download', download))
    updater.dispatcher.add_handler(CommandHandler('dv', download_video))
    
    updater.start_polling()
    updater.idle()

main()