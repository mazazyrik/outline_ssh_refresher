import os

import qrcode
from telegram import Bot, ReplyKeyboardMarkup
from telegram.ext import CommandHandler, Updater

from utils import get_new_key
from transfer_to_db import add_to_db

TOKEN = '7165923004:AAEwtK6AYDj5iFVkse5mkXRMFzgZy_zYt9k'
update = Updater(TOKEN)

bot = Bot(TOKEN)


def make_qr(data, name):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    file_name = f'{name}.jpg'

    img.save(file_name)

    return file_name


def wake_up(update, context):
    chat = update.effective_chat

    button = ReplyKeyboardMarkup([['/newssh']], resize_keyboard=True)

    context.bot.send_message(
        chat_id=chat.id,
        text=(
            'Привет! Криптоферма работает в штатном режиме. Готов выдать ключ '
        ),
        reply_markup=button
    )
    add_to_db(chat.id)


def new_ssh(update, context):
    chat = update.effective_chat
    name = update.message.chat.first_name

    ssh = get_new_key(name)

    qr = make_qr(ssh.access_url, name)

    context.bot.send_message(
        chat_id=chat.id,
        text='Бро, держи твой ключ, ты этого заслужил'
    )

    context.bot.send_message(
        chat_id=chat.id,
        text=ssh.access_url
    )

    context.bot.send_photo(chat.id, open(qr, 'rb'))
    os.remove(qr)


def main():
    updater = Updater(TOKEN)

    updater.dispatcher.add_handler(CommandHandler('start', wake_up))
    updater.dispatcher.add_handler(CommandHandler('newssh', new_ssh))
    bot.send_message(387435447, 'Бот запущен')

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
