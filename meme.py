import requests
from bs4 import BeautifulSoup

def get_random_image():
    response = requests.get('https://www.anekdot.ru/random/mem/')
    soup = BeautifulSoup(response.content, 'html.parser')
    image_element = soup.select('.topicbox img')[0]
    image_url = image_element['src']
    return image_url