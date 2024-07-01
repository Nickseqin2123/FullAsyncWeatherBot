import aiohttp
import datetime

from API import API


async def get_weather(punct):
    url = f'https://api.openweathermap.org/data/2.5/weather?q={punct}&lang=ru&appid={API}&units=metric'
    async with aiohttp.ClientSession() as session:
        async with session.get(url=url) as req:
            data = await req.json()
            city = data['name']
            temper = data['main']['temp']
            humidity = data['main']['humidity']
            pressure = data['main']['pressure']
            wind = data['wind']['speed']
            length_day = datetime.datetime.fromtimestamp(data['sys']['sunset']) - datetime.datetime.fromtimestamp(
                data['sys']['sunrise'])
            
            return f'''Сейчас: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}
Погода в городе: {city}
Температура: {temper}C°
Влажность: {humidity} %
Давление: {pressure} мм.рт.ст
Ветер: {wind} м/с
Продолжительность дня: {length_day}
Хорошего дня!
'''