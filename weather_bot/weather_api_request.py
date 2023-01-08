import pprint
import datetime
import requests
from config import token_weather


def get_weather(city, token):

    code_to_smile = {
        'Clear': 'Ясно \U00002600',
        'Clouds': 'Облачно \U00002601',
        'Rain': 'Дождь \U00002614',
        'Drizzle': 'Дождь \U00002614',
        'Thunderstorm': 'Гроза \U000026A1',
        'Snow': 'Снег \U0001F328',
        'Mist': 'Туман \U0001F32B'
    }

    try:
        r = requests.get(url=f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={token}&units=metric')
        data = r.json()

        city = data['name']
        current_temp = data['main']['temp']

        weather_description = data['weather'][0]['main']
        if weather_description in code_to_smile:
            wd = code_to_smile[weather_description]
        else:
            wd = 'Посмотри в окно, не пойму что там за погода!!!'

        humidity = data['main']['humidity']
        pressure = data['main']['pressure']
        wind = data['wind']['speed']

        sunrise_timestamp = datetime.datetime.fromtimestamp(data['sys']['sunrise'])
        sunset_timestamp = datetime.datetime.fromtimestamp(data['sys']['sunset'])

        length_of_the_day = sunset_timestamp - sunrise_timestamp

        print(f'***{datetime.datetime.now().strftime("%Y-%m-%d %H:%M")}***\n'
              f'Погода в городе: {city}\n'
              f'Температура: {current_temp}°C {wd}\n'
              f'Влажность: {humidity}%\n'
              f'Давление: {pressure} мм.рт.ст\n'
              f'Ветер: {wind} м\c\n'
              f'Восход солнца: {sunrise_timestamp}\n'
              f'Закат солнца: {sunset_timestamp}\n'
              f'Продолжительность дня: {length_of_the_day}\n'
              f'Хорошего дня!!!')

        # pprint.pprint(data)
    except Exception as exc:
        print(exc)
        print('Проверьте название города')


def main():
    city = input('Введите название города: ')
    get_weather(city, token_weather)


if __name__ == '__main__':
    main()
