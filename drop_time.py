from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.types import ParseMode
from aiogram.utils import executor
from apscheduler.schedulers.asyncio import AsyncIOScheduler
import sqlite3
import datetime

def get_datadb():
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM Users')
    users = cursor.fetchall()
    data_db = []

    for user in users:
        id = user[1]
        name = user[2]
        time = user[5]
        city = user[4]
        data_db.append([id, name, time, city])

    connection.close()
    return data_db