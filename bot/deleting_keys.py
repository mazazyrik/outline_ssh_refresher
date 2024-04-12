import logging

import schedule
from db_connect import Database
from main import bot
from utils import delete_all_keys


def delete_keys() -> None:
    '''
    This scripts deletes all active keys.
    '''
    logging.info('Deleting script started')
    delete_all_keys()
    db = Database().get_ids()
    for id in db:
        bot.send_message(
            chat_id=id,
            text=(
                'Все ключи удалены! Стоит задуматься о получении новых ключей.'
            )
        )
    logging.info('All messages had been send')


def newsletter() -> None:
    logging.info('Newsletter started')
    db = Database().get_ids()
    for id in db:
        bot.send_message(
            chat_id=id,
            text=(
                'Всем привет! Заработала последняя и самая новая версия бота!'
                'Теперь каждый раз бот будет предупреждать об удалении ключей '
                'и о других новостях'
            )
        )
    logging.info('Newslettter finished')


schedule.every(1).sunday.at("21:00").do(delete_keys)


while True:
    schedule.run_pending()
