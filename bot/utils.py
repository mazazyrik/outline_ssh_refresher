import logging
import os

from dotenv import load_dotenv

from db_connect import Database
from outline_vpn import OutlineVPN

load_dotenv()

client = OutlineVPN(api_url=os.getenv('API'),
                    cert_sha256=os.getenv('SSH'))


def get_new_key(name: str):
    '''
    This func issues new key, and names it as client username.
    '''
    new_key = client.create_key()
    client.rename_key(new_key.key_id, name)
    return new_key


def delete_all_keys():
    '''
    This func deletes all keys.
    '''
    for key in client.get_keys():
        client.delete_key(key.key_id)


def get_all_keys():
    '''
    This func returns all keys, provided by server.
    '''
    return [key.name for key in client.get_keys()]


def delete_key(name: str):
    '''
    This func delete a key with provided name.
    '''
    for key in client.get_keys():
        if key.name == name:
            client.delete_key(key.key_id)
            return True


def all_keys_str():
    '''
    This func returns all keys, as a str.
    It is easier to send it as a message in bot.
    '''
    all_keys = ''
    for i, name in enumerate(get_all_keys()):
        if i == len(get_all_keys())-1:
            all_keys += f'{name}'
        else:
            all_keys += f'{name}, '
    return all_keys


def newsletter(bot) -> None:
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
