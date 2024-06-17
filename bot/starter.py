import sys
from pathlib import Path
import os
import subprocess

project_root = Path(__file__).resolve().parent.parent
sys.path.append(str(project_root / 'backend' / 'src'))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

import django

django.setup()

import telebot
import art
from auth_user.models.user import EsUser

bot_token = '7427993148:AAFZKryDQ8pUBQzwRn4A3b6UdYjH-a3m_bQ'
bot_runner = telebot.TeleBot(bot_token)

is_auth_in_bot = False
attempts = 4
ban_list = set()


@bot_runner.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id
    if user_id in ban_list:
        bot_runner.send_message(user_id, 'Вы заблокированы и не можете использовать бота.')
    else:
        bot_runner.send_message(user_id, 'Привет! Я МегаБот, который зарегистрирует твой ПК в системе MegaAdmin')


@bot_runner.message_handler(content_types=['text'])
def handle_text(message):
    global is_auth_in_bot
    user_id = message.from_user.id

    if user_id in ban_list:
        bot_runner.send_message(user_id, 'Вы заблокированы и не можете использовать бота.')
        return

    if message.text == '/start':
        request_password(user_id)

    elif not is_auth_in_bot:
        authenticate_user(user_id, message.text)

    elif message.text == '/req':
        register_user(user_id)
        script = subprocess.Popen(
            ["powershell.exe",
             "C:\\Users\\thepr\\PycharmProjects\\MegaBot\\Scripts\\get_info_os.ps1"],
            stdout=sys.stdout
        )
        script.communicate()
        bot_runner.send_message(user_id, text=f'Ник: {script}')


def request_password(user_id):
    bot_runner.send_message(user_id, 'Введите пароль, который вам дал админ: ')


def authenticate_user(user_id, text):
    global is_auth_in_bot
    global attempts

    if text == '1234':
        is_auth_in_bot = True
        bot_runner.send_message(user_id, 'Пароль верный. Введите /req, чтобы зарегистрироваться.')
    else:
        attempts -= 1
        bot_runner.send_message(user_id, f'Неправильный пароль. Осталось попыток: {attempts}')
        if attempts <= 0:
            bot_runner.send_message(user_id, 'Ваша учетная запись заблокирована.')
            ban_list.add(user_id)


def register_user(user_id):
    try:
        user = EsUser(username=str(user_id))
        user.save()

        bot_runner.send_message(user_id, f'Вы зарегистрированы в системе MegaAdmin. Ваш пароль: {user.password}')
    except Exception as e:
        bot_runner.send_message(user_id, 'Произошла ошибка при регистрации. Попробуйте еще раз позже.')
        print(f'Error during user registration: {e}')


if __name__ == '__main__':
    art.tprint(f'bot is running...'.upper(), space=2)
    bot_runner.polling(none_stop=True, interval=0)
