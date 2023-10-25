import telebot
import main

TOKEN = "6325354154:AAEWAiTteahfSlGjydFDgYVvh56i0ZdJCvw"
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome(message):
	sms = main.main()
	bot.reply_to(message, sms)


if __name__ == '__main__':
	bot.infinity_polling()

