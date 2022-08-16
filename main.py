from telegram.ext import CommandHandler
from telegram.ext import Updater

from commands import *

updater = Updater('Token')
updater.dispatcher.add_handler(CommandHandler('hi', hi_command))
updater.dispatcher.add_handler(CommandHandler('help', help_command))
updater.dispatcher.add_handler(CommandHandler('calc', calc_command))
print('server start')
updater.start_polling()
updater.idle()