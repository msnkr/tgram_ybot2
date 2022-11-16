
from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='I am a bot. Type {/audio {artist song}} to search artist and song name audio. Type {/video {artist video}} to search artist and song video. You will recieve a message when the file is ready for download. Example {/video Joji Gimme Love}, {/audio Joji Gimme Love}. Press {/help} for a list of current problems. ')


def help(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='Takes long to download: The Youtube-dl api seems to be capped at 50Kpbs. Unfortunately there isn\'t much I can do about this. The original maintainer of the repo would have to fix this. I might try bypass youtube-dl but that is for a future release. ')



def main():
    updater = Updater(token='TOKEN')
    dispatcher = updater.dispatcher
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)

    updater.dispatcher.add_handler(CommandHandler('help', help))
    updater.dispatcher.add_handler(CommandHandler('audio', get_audio_url))
    updater.dispatcher.add_handler(CommandHandler('video', get_video_url))
    updater.dispatcher.add_handler(CommandHandler('da', get_audio))
    updater.dispatcher.add_handler(CommandHandler('dv', get_video))

    updater.start_polling()
    updater.idle()