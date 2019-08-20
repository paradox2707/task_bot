import telebot
TOKEN = '870672383:AAE9d8p3SRMrMV3L15RwRzYZwVDThCLPS4g'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.send_message(message.chat.id, f"Hi, {message.chat.first_name}")

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