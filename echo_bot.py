
import datetime

import calendar
from telegramcalendar import create_calendar
import telebot
from telebot import types



TOKEN = '870672383:AAE9d8p3SRMrMV3L15RwRzYZwVDThCLPS4g'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.send_message(message.chat.id, f"Hi, {message.chat.first_name}")

@bot.message_handler(commands = ['url'])
def url(message):
    markup = types.InlineKeyboardMarkup()
    btn_my_site= types.InlineKeyboardButton(text='Наш сайт', url='https://habrahabr.ru')
    markup.add(btn_my_site)
    bot.send_message(message.chat.id, "Нажми на кнопку и перейди на наш сайт.", reply_markup = markup)

@bot.message_handler(commands = ['switch'])
def switch(message):
    markup = types.InlineKeyboardMarkup()
    switch_button = types.InlineKeyboardButton(text='Try', switch_inline_query="Telegram")
    markup.add(switch_button)
    bot.send_message(message.chat.id, "Выбрать чат", reply_markup = markup)
    print(markup)

@bot.message_handler(commands=['calendar'])
def get_calendar(message):
    now = datetime.datetime.now() #Текущая дата
    chat_id = message.chat.id
    date = (now.year, now.month)
    #current_shown_dates = {}
    #current_shown_dates[chat_id] = date #Сохраним текущую дату в словарь
    markup = types.InlineKeyboardMarkup()
    row_set = create_calendar(now.year,now.month)

    for i in row_set:
        markup.row(*i)
    bot.send_message(message.chat.id, "Пожалйста, выберите дату", reply_markup=markup)


@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, "Спробуй команди /start /help /url /switch /calendar")
	print(message)


# @bot.message_handler(func=lambda message: True)
# def echo_all(message):
# 	bot.reply_to(message, message.text)
#
# @bot.message_handler(content_types=['text'])
# def send_welcome(message):
# 	bot.reply_to(message, "Really?")

bot.polling()