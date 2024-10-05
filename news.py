import requests
import random
from datetime import datetime

def news(request):

    request = request
    
    m = str(int(datetime.today().strftime("%m")) - 1)
    today = str(datetime.today().strftime(f'%Y-{m}-%d'))

    API_KEY = "YourAPIKey"
    url = f"https://newsapi.org/v2/everything?q={request}&from={today}&sortBy=publishedAt&apiKey={API_KEY}"
    news_data = requests.get(url).json()
    try:
        if len(news_data['articles']) == 0:
            return "По вашему запросу ничего не найдено"
        else:
            r = random.randint(0,len(news_data['articles'])-1)
            author = news_data['articles'][r]['author']
            title = news_data['articles'][r]['title']
            description = news_data['articles'][r]['description']
            new_url = news_data['articles'][r]['url']

            return f'НОВОСТЬ ПО ЗАПРОСУ {request} \n\nАВТОР СТАТЬИ: {author} \n\n{title} \n\n{description} \n\nСсылка на статью: {new_url}'
    except:
        return 'Непредвиденная ошибка'
