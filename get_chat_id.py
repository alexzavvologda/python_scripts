# telegram
# https://core.telegram.org/bots/api
import telebot
import json
import requests
#pip3 install pyTelegramBotAPI

# чтобы узнать ID чата вставляем токен запускаем и в телеге ищем бота и пишем ему старт
 

# alexzav_monitoring
TOKEN ='1999999999999:AAwerdfggdghtyhrhdgffdW2I'
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет я тут /help")
    bot.reply_to(message, 'чат ид - ' + str(message.chat.id))

@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message, "получаем информацию по id чата")
    bot.reply_to(message, 'чат ид - ' + str(message.chat.id))


bot.polling()
