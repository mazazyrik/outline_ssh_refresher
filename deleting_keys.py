import schedule
from utils import delete_all_keys
from main import bot

f = open('db.txt', 'r')
db = [int(i) for i in f]


def delete_keys():
    delete_all_keys()
    for id in set(db):
        print(id)
        bot.send_message(
            id,
            'Все ключи удалены! Стоит задуматься о получении новых ключей.'
        )


schedule.every(1).sunday.at("21:00").do(delete_keys)

while True:
    schedule.run_pending()
