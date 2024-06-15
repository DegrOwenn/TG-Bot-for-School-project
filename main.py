'''pip install aiogram==2.25.1, pip install googletrans==3.1.0a0'''
from weather import weather
from finance import currencies
from fact import fact
from meme import get_random_image
from holiday import holiday
from news import news
from citation import quote

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from apscheduler.schedulers.asyncio import AsyncIOScheduler
import asyncio

from apscheduler.schedulers.asyncio import AsyncIOScheduler, asyncio
from datetime import datetime, timedelta
import logging
import markups as mp
from register import Users

from drop_time import get_datadb
from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext

TOKEN = 'Your TOKEN'

logging.basicConfig(level=logging.INFO)
bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())
users = Users('data.db')

from aiogram.dispatcher.filters.state import StatesGroup, State

class UserState(StatesGroup):
    new = State()
    newcity = State()
    newschedule = State()
    city_weather = State()

admin = [1234,1234] # Use your Telegram IDs here

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    if (not users.exists_or_not(message.from_user.id)):
        users.new_user(message.from_user.id)
        await bot.send_message(message.from_user.id, "Ваше имя: ")
    else:
        await bot.send_message(message.from_user.id, "Вы зарегестрированы.\n\nПримечание: Вы можете настроить город в котором Вы живёте, и расписание того, во сколько присылать Вам ту или иную информацию в НАСТРОЙКАХ!", reply_markup=mp.mainMenu)



@dp.message_handler(commands=['as'])
async def autosend(message: types.Message):
    if message.from_user.id in admin:
        global data_db
        data_db = get_datadb()
        while True:
            await asyncio.sleep(1)
            now = datetime.now()
            current_time = now.strftime("%H:%M")
            print(current_time)
            for i in data_db:
                if current_time in i:
                    await bot.send_message(chat_id=str(i[0]),text=f'Доброго времени суток {i[1]}, сейчас на улице города {weather(str(i[3]))}')
                    await asyncio.sleep(60)
                

@dp.message_handler()
async def bot_message(message: types.Message):

    if message.chat.type == "private":

        #Вызов меню
        if message.text == "Функции":
            await bot.send_message(message.from_user.id, "Функции!", reply_markup=mp.functionMenu)
        elif message.text == "Настройки":
            await bot.send_message(message.from_user.id, "Мы в настройках!", reply_markup=mp.settingMenu)
        elif message.text == "Вернуться":
            await bot.send_message(message.from_user.id, "Вернулись!", reply_markup=mp.mainMenu)
        elif message.text == "Сбросить настройки":
            await bot.send_message(message.from_user.id, users.reset_schedule(message.from_user.id, "выкл"))
            global data_db
            data_db = get_datadb()
            print(data_db)

        #Вызов функций

        #Приылает подробную погоду на сегодня
        elif message.text == "Погода":
            await bot.send_message(message.from_user.id, "В каком городе узнать погоду?")
            await UserState.city_weather.set()

        #Присылает текущие курсы валют
        elif message.text == "Валюты":
            await bot.send_message(message.from_user.id, currencies())

        #Пришлёт интересный факт
        elif message.text == "Факт":
            await bot.send_message(message.from_user.id, fact())

        #Скинет мем
        elif message.text == "Мем":
            await bot.send_message(message.from_user.id, f'<tg-spoiler>{get_random_image()}</tg-spoiler>',parse_mode="HTML")

        #Скажет, когда в этом месяце выходные
        elif message.text == "Выходные":
            await bot.send_message(message.from_user.id, await holiday(""))

        #Пришлёт новость на выбранную вами тему
        elif message.text == "Новость":
            await bot.send_message(message.from_user.id, "О чём хотели бы узнать?")
            await UserState.new.set()


        #Скинет мем
        elif message.text == "Цитата":
            await bot.send_message(message.from_user.id, quote())

        #Настройки (названия оправдывают функционал)
        elif message.text == "Сменить город":
            await bot.send_message(message.from_user.id, "Какой теперь город?")
            await UserState.newcity.set()

        elif message.text == "Сменить расписание":
            await bot.send_message(message.from_user.id, "Теперь когда присылаем?")
            await UserState.newschedule.set()


        #Регистрация
        else:
            if users.get_signup(message.from_user.id) == "setname":
                if len(message.text) > 16:
                    await bot.send_message(message.from_user.id, "Чета многа букав, давай до 16 букав")
                elif "@" in message.text or "/" in message.text:
                    await bot.send_message(message.from_user.id, "Плохие символы '@' и '/' низя")
                else:
                    users.set_name(message.from_user.id, message.text)
                    users.set_signup(message.from_user.id, "done")
                    await bot.send_message(message.from_user.id, "Теперь вы зарегестрированы.\n\nПримечание: Вы можете настроить город в котором Вы живёте, и расписание того, во сколько присылать Вам ту или иную информацию в НАСТРОКАХ!", reply_markup=mp.mainMenu)
            else:
                await bot.send_message(message.from_user.id, "ты че несешь, по-русски говори")


#Какую новость прислать
@dp.message_handler(state=UserState.new)
async def set_new(message: types.Message, state: FSMContext):
    await state.update_data(new=message.text)
    data = await state.get_data()
    await bot.send_message(message.from_user.id, news(data['new']))
    await state.finish()


#Смена города
@dp.message_handler(state=UserState.newcity)
async def set_new(message: types.Message, state: FSMContext):
    await state.update_data(newcity=message.text)
    data = await state.get_data()
    await bot.send_message(message.from_user.id, users.set_city(message.from_user.id, data["newcity"]))
    global data_db
    data_db = get_datadb()
    print(data_db)
    await state.finish()


#Смена расписания
@dp.message_handler(state=UserState.newschedule)
async def set_new(message: types.Message, state: FSMContext):
    await state.update_data(newschedule=message.text)
    data = await state.get_data()
    await bot.send_message(message.from_user.id, users.set_schedule(message.from_user.id, data["newschedule"]))
    global data_db
    data_db = get_datadb()
    print(data_db)
    await state.finish()


#Присыл погоды нужного города
@dp.message_handler(state=UserState.city_weather)
async def set_new(message: types.Message, state: FSMContext):
    await state.update_data(city_weather=message.text)
    data = await state.get_data()
    await bot.send_message(message.from_user.id, weather(data["city_weather"]))
    await state.finish()


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)