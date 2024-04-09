import schedule

from db_connect import get_ids
from main import bot
from utils import delete_all_keys


def delete_keys() -> None:
    delete_all_keys()
    print('work')
    db = get_ids()
    for id in set(*db):
        bot.send_message(
            chat_id=id,
            text=(
                'Все ключи удалены! Стоит задуматься о получении новых ключей.'
            )
        )


schedule.every(1).monday.at("13:57").do(delete_keys)


while True:
    schedule.run_pending()
