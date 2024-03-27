import schedule
import telegram
from utils import delete_all_keys
from main import db, TOKEN


bot = telegram.Bot(TOKEN)


def delete_keys():
    delete_all_keys()
    for id in db:
        bot.send_message(
            id,
            'Все ключи удалены! Стоит задуматься о получении новых ключей.'
        )


schedule.every(1).monday.at("10:00").do(delete_all_keys)

while True:
    schedule.run_pending()
