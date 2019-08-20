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



@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, "Катя, я тебе кохаю! ♥")
	print(message)


# @bot.message_handler(func=lambda message: True)
# def echo_all(message):
# 	bot.reply_to(message, message.text)
#
# @bot.message_handler(content_types=['text'])
# def send_welcome(message):
# 	bot.reply_to(message, "Really?")

bot.polling()