import requests

def weather(city):

    url = 'https://api.openweathermap.org/data/2.5/weather?q='+city+'&units=metric&lang=ru&appid=79d1ca96933b0328e1c7e3e7a26cb347'
    try:
        weather_data = requests.get(url).json()
        temperature = round(weather_data['main']['temp'])
        temperature_feels = round(weather_data['main']['feels_like'])
        wind_speed = round(weather_data['wind']['speed'])
        pressure = round(weather_data['main']['pressure'])
        deg = round((weather_data['wind']['deg'])/45)
        description = weather_data['weather'][0]['description']
        humidity = round(weather_data['main']['humidity'])

        if deg == 0:
            way = "С"
        elif deg == 1:
            way = "СВ"
        elif deg == 2:
            way = "В"
        elif deg == 3:
            way = "ЮВ"
        elif deg == 4:
            way = "Ю"
        elif deg == 5:
            way = "ЮЗ"
        elif deg == 6:
            way = "З"
        elif deg == 7:
            way = "СЗ"
        
        return f"{city}\n\n1. Температура: {str(temperature)}°C, Ощущается как: {str(temperature_feels)}°C\n2. Погода: {str(description)}\n3. Влажность: {str(humidity)} г/м³\n4. Скорость ветра: {str(wind_speed)} м/c, Направление: {str(way)}\n5. Давление: {str(round(pressure/1.33322,0))} мм. рт. ст. / {str(pressure)} мбар"
    except:
        return "Извините, такого города нет"