import asyncio
from googletrans import Translator

from datetime import date, datetime
from isdayoff import DateType, ProdCalendar

calendar = ProdCalendar(locale='ru')
translator = Translator()

month_ = datetime.now()
month_ = month_.strftime("%B")
month = translator.translate(month_, dest='ru')

today = datetime.today().strftime('%Y.%m.%d')

async def holiday(holidayList):

    global today
    holiday_list = holidayList
    holiday_data = await calendar.month(date(datetime.now().year, datetime.now().month, 1))
    for i in holiday_data:
        if holiday_data[i] == DateType.NOT_WORKING:
            holiday_list += f"{str(i)[8]}{str(i)[9]} \n"
    if holiday_data[today] == DateType.NOT_WORKING:
        today = "Сегодня ВЫХОДНОЙ"
    else:
        today = "Сегодня НЕ выходной"
    return f"Вот числа выходных дней на {month.text.capitalize()}:\n\n{today}\n\n{holiday_list}"