import requests


def currencies():

  BITOC = requests.get(
      'https://api.coindesk.com/v1/bpi/currentprice.json').json()
  dataNatVal = requests.get(
      'https://www.cbr-xml-daily.ru/daily_json.js').json()
  USD = str(round(dataNatVal['Valute']['USD']['Previous'], 2))
  EUR = str(round(dataNatVal['Valute']['EUR']['Previous'], 2))
  KZT = str(round(dataNatVal['Valute']['KZT']['Previous'], 1) / 100)
  BYN = str(round(dataNatVal['Valute']['BYN']['Previous'], 2))
  btcRate = BITOC["bpi"]['USD']['rate']
  btcRate = btcRate.replace(",", " ")
  return f'$ USD: {USD} руб \n€ EUR: {EUR} руб \n₿ BTC: {btcRate} USD\n₸  KZT: {KZT} руб\nBr BYN: {BYN} руб'
