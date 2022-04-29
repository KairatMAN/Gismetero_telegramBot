import requests
import datetime
from pprint import pprint
from main.data_generator.config import open_weather_token



def get_weather(city, open_weather_token):

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
            f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}&units=metric"
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

        return print(f"***{datetime.datetime.now().strftime('%Y-%m-%d**%H:%M')}***\n"
              f"Погода в городе: {city}\nТемпература: {cur_weather} °C {wd}\n"
              f"Влажность: {humidity}%\nДавление: {pressure}мм.рт.ст.\nСкорость ветра: {wind_speed}м/сек\nВосход солнца: {sunrise}\n"
              f"Закат солнца: {sunset}\nДлительность дня: {lenght_of_day}\n"
              f"Хорошего вам дня!")




    except Exception as ex:
        print(ex)
        print("Проверьте правильность введенных данных")


def main():

    city = input("Введите город: ")

    # while city_in in Kyrgyzstan == False:
    #     city_in = input("Город не найден в базе данных, введите название другого города: ")
    #
    # lat = Kyrgyzstan[city_in][0]
    # lon = Kyrgyzstan[city_in][1]

    get_weather(city, open_weather_token)


if __name__ == "__main__":
    main()
