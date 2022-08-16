from telegram import Update
from telegram.ext import CallbackContext
from logger import log


def hi_command(update: Update, context: CallbackContext):
    log(update, context)
    update.message.reply_text(f'Hi {update.effective_user.first_name}!')

def help_command(update: Update, context: CallbackContext):
    log(update, context)
    update.message.reply_text(f'Калькулятор производит следующие действия над числами, в том числе с комплексными:'
                              f'\nсложение "+", вычитание "-", умножение "*", деление"/", возведение в степень"**", остаток от деления "%"'
                              f'\nпосле команды /calc между числами и действием необходимо ставить пробел, пример /calc 5 ** 2 или /calc 2-3j + 23+7j')

def calc_command(update: Update, context: CallbackContext):
    log(update, context)
    msg = update.message.text
    print(msg)
    items = msg.split()
    x = items[1]
    action = items[2]
    y = items[3]
    exept = x + action + y
    result=eval(exept)
    print(f'{exept} = {result}')
    update.message.reply_text(f'{x} {action} {y} = {result}')