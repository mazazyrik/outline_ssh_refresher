import schedule

from db_connect import get_ids
from main import bot
from utils import delete_all_keys


def delete_keys():
    delete_all_keys()
    db = get_ids()
    for id in set(db):
        print(id)
        bot.send_message(
            id,
            'Все ключи удалены! Стоит задуматься о получении новых ключей.'
        )


schedule.every(1).sunday.at("21:00").do(delete_keys)

print(get_ids())

while True:
    schedule.run_pending()
