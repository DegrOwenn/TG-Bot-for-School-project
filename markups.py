from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

#Кнопки
functionBtn = KeyboardButton("Функции")
settingsBtn = KeyboardButton("Настройки")
returnBtn = KeyboardButton("Вернуться")

weatherBtn = KeyboardButton("Погода")
financeBtn = KeyboardButton("Валюты")
factBtn = KeyboardButton("Факт")
memeBtn = KeyboardButton("Мем")
holidayBtn = KeyboardButton("Выходные")
newsBtn = KeyboardButton("Новость")
citationBtn = KeyboardButton("Цитата")
resetBtn = KeyboardButton("Сбросить настройки")


changeCityBtn = KeyboardButton("Сменить город")
changeScheduleBtn = KeyboardButton("Сменить расписание")

#Менюшки
mainMenu = ReplyKeyboardMarkup(resize_keyboard=True)
mainMenu.add(functionBtn, settingsBtn)

functionMenu = ReplyKeyboardMarkup(resize_keyboard=True)
functionMenu.add(weatherBtn).add(newsBtn).add(financeBtn).add(memeBtn).add(factBtn).add(holidayBtn).add(citationBtn).add(returnBtn)   #, newsBtn, financeBtn, factBtn, memeBtn, holidayBtn, citation, returnBtn)

settingMenu = ReplyKeyboardMarkup(resize_keyboard=True)
settingMenu.add(changeCityBtn, changeScheduleBtn).add(resetBtn).add(returnBtn)
