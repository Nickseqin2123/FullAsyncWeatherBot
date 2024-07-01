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
            description = data['weather'][0]['description'].capitalize()
            
            return f'''Сейчас: {datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=3))).strftime('%Y-%m-%d %H:%M')} по МСК
{'-' * 60}
Погода в городе: {city}
На улице: {description}

Температура воздуха: {temper}C°
Влажность: {humidity}%

Давление: {pressure} мм.рт.ст
Ветер: {wind} м/с

Продолжительность дня: {length_day}
Хорошего дня!
'''