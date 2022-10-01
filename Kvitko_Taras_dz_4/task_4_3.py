import xml.etree.ElementTree as ET
from datetime import datetime, date

import requests
from requests import utils


def currency_rates_adv(code: str) -> (float, date):
    url = 'http://www.cbr.ru/scripts/XML_daily.asp'
    response = requests.get(url)
    if response.status_code != 200:
        print(f'Error: HTTP {response.status_code}')
        return None, None
    else:

        encodings = utils.get_encoding_from_headers(response.headers)
        content = response.content.decode(encoding=encodings)
        tree = ET.ElementTree(ET.fromstring(content))
        root = tree.getroot()

        date_ = datetime.strptime(root.attrib['Date'], '%d.%m.%Y')

        for currency in tree.getroot():
            # среди всех курсов ищем нужную валюту
            currency_dict = dict()
            for param in currency:
                significant_fields = ['CharCode', 'Value', 'Nominal']  # значимые для алгоритма поля
                if param.tag in significant_fields:  # идем по полям объекта валюты
                    currency_dict[param.tag] = param.text  # значимые поля заносим в словарь
                    if currency_dict['CharCode'] == code.upper() and \
                            'Value' in currency_dict and \
                            'Nominal' in currency_dict:
                        # если это нужный код и уже собрана стоимость и номинал, возвращаем стоимость

                        currency = float(currency_dict['Value'].replace(',', '.')) / float(currency_dict['Nominal'])
                        return currency, date_.date()

        # если в ответе не нашелся запрошенный код валюты, возвращаем только дату
        return None, date_


rate, date_value = currency_rates_adv("USD")

empty = bool(not rate and not date_value)
if not empty and not isinstance(rate, float):
    raise TypeError("Неверный тип данных у курса")
if not empty and not isinstance(date_value, date):
    raise TypeError("Неверный тип данных у даты")
print(rate, date_value)
