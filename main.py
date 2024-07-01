import asyncio
import logging

from aiogram import Dispatcher, Bot
from aiogram.types import Message
from aiogram.filters.command import CommandStart
from main_router import router as main_router
from Keyboards.keyb import get_weather_keyb


dp = Dispatcher()
dp.include_router(
    main_router
)


@dp.message(CommandStart())
async def go_start(message: Message):
    await message.answer(
        text='Привет, я бот который присылает погоду.',
        reply_markup=await get_weather_keyb()
        )


async def main():
    logging.basicConfig(level=logging.INFO)
    bot = Bot(token='')
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())