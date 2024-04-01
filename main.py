import os

import qrcode
from telegram import Bot, ReplyKeyboardMarkup
from telegram.ext import (CommandHandler, ConversationHandler, Filters,
                          MessageHandler, Updater)

from transfer_to_db import add_to_db
from utils import all_keys_str, delete_key, get_all_keys, get_new_key

TOKEN = '7165923004:AAEwtK6AYDj5iFVkse5mkXRMFzgZy_zYt9k'
DELETE_KEY = 1


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
    name = update.message.chat.first_name

    button = ReplyKeyboardMarkup(
        [['/newssh'], ['/admin']], resize_keyboard=True
    )

    context.bot.send_message(
        chat_id=chat.id,
        text=(
            'Привет! Криптоферма работает в штатном режиме. Готов выдать ключ '
        ),
        reply_markup=button
    )
    if name not in get_all_keys():
        context.bot.send_video(
            chat_id=chat.id,
            video=open('inst.MP4', 'rb'),
            supports_streaming=True
        )
        add_to_db(chat.id)
        context.bot.send_message(
            chat_id=chat.id,
            text=(
                'Невероятная инструкция выше!'
            ),
            reply_markup=button
        )


def new_ssh(update, context):
    chat = update.effective_chat
    name = update.message.chat.first_name

    if name not in get_all_keys():

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
    else:
        context.bot.send_message(
            chat_id=chat.id,
            text=(
                f'{name} уже имеет ключ! вы не можете иметь несколько ключей'
            )
        )


def admin(update, context):
    chat = update.effective_chat

    if chat.id == 387435447:
        keys_button = ReplyKeyboardMarkup(
            [['/allkeys'], ['/deletekey'], ['/start']], resize_keyboard=True)

        context.bot.send_message(
            chat_id=chat.id,
            text='Привет, Никита! Вот тебе твои инструменты',
            reply_markup=keys_button
        )
    else:
        context.bot.send_message(
            chat_id=chat.id,
            text='Вы не админ бе бе бе',
        )


def all_keys(update, context):
    chat = update.effective_chat
    if chat.id == 387435447:

        context.bot.send_message(chat_id=chat.id, text=all_keys_str())
    else:
        context.bot.send_message(chat_id=chat.id, text='Руки прочь!')


def cancel(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Операция отменена. Чтобы удалить другой ключ, повторите команду."
    )
    return ConversationHandler.END


def delete_smbd_key(update, context):
    chat = update.effective_chat
    if chat.id == 387435447:

        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Напишите ник пользователя, чей ключ надо удалить"
        )

        return DELETE_KEY
    else:
        context.bot.send_message(chat_id=chat.id, text='Руки прочь!')


def handle_new_message(update, context):
    name = update.message.text
    status = delete_key(name)
    if status:
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=f'Ключ пользователя {name} успешно удален!'
        )
    else:
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text='Такого пользователя нет!'
        )
    return ConversationHandler.END


conversation_handler = ConversationHandler(
    entry_points=[MessageHandler(
        ~Filters.command, handle_new_message)],
    states={
        DELETE_KEY: [MessageHandler(
            Filters.text & ~Filters.command, handle_new_message
        )],
    },
    fallbacks=[CommandHandler('cancel', cancel)],
)


def main():
    updater = Updater(TOKEN)

    updater.dispatcher.add_handler(CommandHandler('start', wake_up))
    updater.dispatcher.add_handler(CommandHandler('newssh', new_ssh))
    updater.dispatcher.add_handler(CommandHandler('admin', admin))
    updater.dispatcher.add_handler(CommandHandler('allkeys', all_keys))
    updater.dispatcher.add_handler(
        CommandHandler('deletekey', delete_smbd_key))
    updater.dispatcher.add_handler(conversation_handler)

    bot.send_message(387435447, 'Бот запущен')

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
