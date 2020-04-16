
import datetime

import calendar
from xml.dom.xmlbuilder import _name_xform

from telegramcalendar import create_calendar
import telebot
from telebot import types
import re




TOKEN = '870672383:AAE9d8p3SRMrMV3L15RwRzYZwVDThCLPS4g'
bot = telebot.TeleBot(TOKEN)
global_m_text = []



@bot.inline_handler(lambda query: len(query.query) is 0)
def empty_query(query):
    hint = "Введите ровно 2 числа и получите результат!"



@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(message.chat.id, f"Hi, {message.chat.first_name}")


    # print(message)
    # n_book = Book()
    # n_book.title = 'book5'
    # n_book.add()

    # n_book.author = 'andrii'
    # n_book.pages = 27
    # n_book.published = datetime.datetime.now()
    # n_book.id = 1





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
    #bot.send_message(message.chat.id, "Выбрать чат", reply_markup = markup)
    bot.send_message(message.chat.id, "Выбрать чат", reply_markup=markup)
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


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    bot.answer_callback_query(call.id, text="Дата выбрана")
    print(call.data)
    text_calback = global_m_text[0]
    text_calback = re.sub('@TaskManager_SmartBot', '', text_calback)
    performer = 'Performer:'
    for word in text_calback.split():
        if word[0] == '@':
            performer = performer + ' ' + word
            text_calback = re.sub(word, '', text_calback)
    deadline = call.data.split(';')
    text_calback = text_calback + '\n' + performer + '\n' + 'Deadline: ' + deadline[3] + '.' + deadline[2] + '.' + deadline[1]
    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=text_calback)
    global_m_text.clear()

@bot.message_handler(func=lambda message: message.chat.type != 'private', regexp='@TaskManager_SmartBot')
def echo_task(message):
    global_m_text.append(message.text)
    now = datetime.datetime.now() #Текущая дата
    markup = types.InlineKeyboardMarkup()
    row_set = create_calendar(now.year,now.month)

    for i in row_set:
        markup.row(*i)
    bot.send_message(message.chat.id, "Пожалуйста, выберите дату", reply_markup=markup)

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

