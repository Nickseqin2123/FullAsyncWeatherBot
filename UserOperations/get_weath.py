from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from Keyboards.keyb import go_menu_keyb, get_weather_keyb
from GetWeather.weather import get_weather


router = Router(name=__name__)


class GetUserPunctState(StatesGroup):
    punct = State()
    
    
@router.message(F.text == 'Прислать погоду')
async def weath_stt(message: Message, state: FSMContext):
    await state.set_state(GetUserPunctState.punct)
    
    await message.answer(
        text='Введите ваш населенный пункт:',
        reply_markup=await go_menu_keyb()
    )
    

@router.message(F.text == 'Главное меню')
async def go_menu(message: Message, state: FSMContext):
    current_state = await state.get_state()
    
    if current_state is None:
        return
    
    await state.clear()
    await message.answer(
        text='Мы в меню',
        reply_markup=await get_weather_keyb()
    )


@router.message(GetUserPunctState.punct)
async def get_user_punct(message: Message, state: FSMContext):
    await state.update_data(punct=message.text)
    
    data = await state.get_data()
    
    await state.clear()
    await summary(message, data, state)
    

async def summary(message: Message, data: dict, state: FSMContext):
    try:
        weather = await get_weather(data['punct'])
    except Exception:
        await message.answer(
            text='Произошла ошибка. Введите населенный пункт повторно'
        )
        await state.set_state(GetUserPunctState.punct)
    else:
        
        await message.answer(
            text=weather,
            reply_markup=await get_weather_keyb()
        )