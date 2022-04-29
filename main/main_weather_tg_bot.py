import requests
import datetime
from main.config import *
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor



bt = Bot(token=tg_bot_token)
dp = Dispatcher(bt)

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.reply("Hello, I'm a weather bot. Write me a city and I'll tell you the weather in it.\nПривет, я бот для погоды. Напиши мне город и я подскажу погоду в нем.")




@dp.message_handler()
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

        await message.reply(f"***{datetime.datetime.now().strftime('%Y-%m-%d**%H:%M')}***\n"
                     f"Погода в городе: {city}\nТемпература: {cur_weather} °C {wd}\n"
                     f"Влажность: {humidity}%\nДавление: {pressure}мм.рт.ст.\nСкорость ветра: {wind_speed}м/сек\nВосход солнца: {sunrise}\n"
                     f"Закат солнца: {sunset}\nДлительность дня: {lenght_of_day}\n"
                     f"<<< Хорошего вам дня! >>>")




    except:
        await message.reply("\U00002620 Проверьте название города \U00002620")


if __name__ == '__main__':
    executor.start_polling(dp)

