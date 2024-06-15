import requests
from googletrans import Translator
import requests
translator = Translator()

def quote():
    response = requests.get("https://animechan.xyz/api/random").json()
    citation = str(response['quote'])
    character = str(response['character'])
    anime = str(response['anime'])    
    text = f'{citation} \n\n{character} из аниме {anime}'
    translation = translator.translate(text, dest='ru')
    ans = str(translation.text)

    return ans