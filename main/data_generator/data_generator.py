import requests
import datetime
from main.data_generator.config import open_weather_token
from main.data_generator.lat_long import *



def get_weather(lat, lon, open_weather_token):
    try:
        r = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={open_weather_token}&units=metric"
        )
        data = r.json()
        # pprint(data)

        city = data['name']
        cur_weather = data['main']['temp']
        humidity = data['main']['humidity']
        pressure = data['main']['pressure']
        wind_speed = data['wind']['speed']
        sunrise = datetime.datetime.fromtimestamp(data['sys']['sunrise'])

        return print(f"Погода в городе: {city}\nТемпература: {cur_weather} °C\n"
              f"Влажность: {humidity}%\nДавление: {pressure}мм.рт.ст.\nСкорость ветра: {wind_speed}м/сек\nВосход солнца: {sunrise}\n"
              f"Хорошего вам дня!")




    except Exception as ex:
        print(ex)
        print("Проверьте правильность введенных данных")


def main(message_reply):


    while city_in in Kyrgyzstan == False:
        city_in = input("Город не найден в базе данных, введите название другого города: ")

    lat = Kyrgyzstan[city_in][0]
    lon = Kyrgyzstan[city_in][1]

    get_weather(lat, lon, open_weather_token)


if __name__ == "__main__":
    main()
