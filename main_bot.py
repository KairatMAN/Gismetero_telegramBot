import telebot
from telebot import types

Token = "5148276292:AAEgppprtEsvHS0XKMq0KsHMGvjjODeqB1k"
bot = telebot.TeleBot(Token)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message,
                 "Hello! Welcome to Gismeteo_Bot!\nTo select a language, click on /button \n\nЗдравствуйте! Добро пожаловать на Gismeteo_Bot! \nДля выбора языка нажмите на /button")


# @bot.message_handler(func=lambda m: True)
# def echo_all(message):
#   bot.reply_to(message, message.text)

@bot.message_handler(commands=['button'])
def button_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("English")
    item2 = types.KeyboardButton("Русский")
    markup.add(item1, item2)
    bot.send_message(message.chat.id, 'Choose a language! \nВыберите язык!', reply_markup=markup)


@bot.message_handler(content_types='text')
def message_reply(message):
    if message.text == "English":
        bot.send_message(message.chat.id, "https://www.gismeteo.com/")
    elif message.text == "Русский":
        bot.send_message(message.chat.id, "https://www.gismeteo.ru/")


bot.infinity_polling()