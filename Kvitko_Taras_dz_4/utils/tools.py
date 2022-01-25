import xml.etree.ElementTree as ET
from datetime import datetime

import requests
from requests import utils


def currency_rates(code: str) -> (float, datetime):
    url = 'http://www.cbr.ru/scripts/XML_daily.asp'
    response = requests.get(url)
    encodings = utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)
    tree = ET.ElementTree(ET.fromstring(content))
    root = tree.getroot()

    date = datetime.strptime(root.attrib['Date'], '%d.%m.%Y')

    for currency in tree.getroot():
        # среди всех курсов ищем нужную валюту
        currency_dict = dict()
        for param in currency:
            # идем по полям объекта валюты
            if param.tag == 'CharCode' or param.tag == 'Value':
                # поля кода и стоимости заносим в словарь
                currency_dict[param.tag] = param.text
                if currency_dict['CharCode'] == code.upper() and 'Value' in currency_dict:
                    # если это нужный код и уже собрана стоимость, возвращаем ее
                    return float(currency_dict['Value'].replace(',', '.')), date

    # если в ответе не нашелся запрошенный код валюты, возвращаем только дату
    return None, date


if __name__ == '__main__':
    value, answer_date = currency_rates(code='usb')
    if value:
        print(f'{value:.2f}, {datetime.strftime(answer_date, "%Y-%m-%d")}')
    else:
        print(datetime.strftime(answer_date, "%Y-%m-%d"))
