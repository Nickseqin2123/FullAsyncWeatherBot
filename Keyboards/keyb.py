from aiogram.utils.keyboard import ReplyKeyboardBuilder


async def get_weather_keyb():
    builder = ReplyKeyboardBuilder()
    builder.button(
        text='Прислать погоду'
    )
    
    return builder.as_markup(resize_keyboard=True)


async def go_menu_keyb():
    builder = ReplyKeyboardBuilder()
    builder.button(
        text='Главное меню'
    )
    
    return builder.as_markup(resize_keyboard=True)
