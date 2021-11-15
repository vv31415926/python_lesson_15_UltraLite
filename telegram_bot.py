import telebot
import pprint

TOKEN = '*'

# экземпляр класса Telebot
bot = telebot.TeleBot( TOKEN, parse_mode=None )

# обработчики сообщений ( фильтр )
@bot.message_handler(commands=['start', 'help'])
def send_welcome( message ):
	#pprint.pprint(message)
	#print( message )
	#print(message['json'])
	bot.reply_to(message, "Приветствую! Вы находитесь в боте занятий по Python!")

@bot.message_handler(content_types=['text'])
def send_welcome( message ):
	text = message.text
	bot.reply_to(message, f"Вы прислали текст:\'{text}\'")

bot.polling()