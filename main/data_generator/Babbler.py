import telebot
from telebot import types
import datetime
import requests
from config import *

TOKEN = '5148276292:AAEgppprtEsvHS0XKMq0KsHMGvjjODeqB1k'

bot = telebot.TeleBot(TOKEN)


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
    bot.send_message(message.chat.id, 'Choose your language! \nВыберите себе язык!', reply_markup=markup)


@bot.message_handler(content_types='text')
def message_reply(message):
    # massages = message.text
    # bot.send_message(message.chat.id, massages)
    if message.text == "English":
        bot.send_message(message.chat.id, 'Enter the name of the city!')
    elif message.text == "Русский":
        bot.send_message(message.chat.id, "Введите название города!")

@bot.message_handler()
async def get_weather(message: types.Message):
    code_to_smile = {
        "Clear": "Ясно \U00002600"
        , "Clouds": "Облачно \U00002601"
        , "Rain": "Дождь \U00002614"
        , "Drizzle": "Дождь \U00002614"
        , "Snow": "Снег \U0001F328"
        , "Mist": "Туман \U0001F32B"
        , "Thunderstorm": "Гроза \U000026A1"

    }

    try:
        r = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={open_weather_token}&units=metric"
        )
        data = r.json()
        # pprint(data)

        city = data['name']
        cur_weather = data['main']['temp']

        weather_description = data['weather'][0]['main']
        if weather_description in code_to_smile:
            wd = code_to_smile[weather_description]
        else:
            wd = "Посмотри в окно, не пойму что там за погода"

        humidity = data['main']['humidity']
        pressure = data['main']['pressure']
        wind_speed = data['wind']['speed']
        sunrise = datetime.datetime.fromtimestamp(data['sys']['sunrise'])
        sunset = datetime.datetime.fromtimestamp(data['sys']['sunset'])
        lenght_of_day = sunset - sunrise

        bot.send_message(message.chat.id, f"***{datetime.datetime.now().strftime('%Y-%m-%d**%H:%M')}***\n"
                     f"Погода в городе: {city}\nТемпература: {cur_weather} °C {wd}\n"
                     f"Влажность: {humidity}%\nДавление: {pressure}мм.рт.ст.\nСкорость ветра: {wind_speed}м/сек\nВосход солнца: {sunrise}\n"
                     f"Закат солнца: {sunset}\nДлительность дня: {lenght_of_day}\n"
                     f"<<< Хорошего вам дня! >>>")




    except:
        bot.send_message(message.chat.id, "\U00002620 Проверьте название города \U00002620")



bot.infinity_polling()