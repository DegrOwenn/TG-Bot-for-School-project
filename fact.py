from googletrans import Translator
import requests

translator = Translator()

def fact():

    data = requests.get('https://uselessfacts.jsph.pl/api/v2/facts/random').json()
    text = str(data['text'])
    translation = translator.translate(text, dest='ru')
    return translation.text