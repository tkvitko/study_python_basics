import os
import re


def parse_log_string(log_string: str) -> tuple:
    """
    Функция парсинга строки лога nginx
    :param log_string: строка лога
    :return: кортеж значений

    Регулярные выражения по блокам:
    IPv4 или IPv6 = (?:\d{,3}\.?){4}|[a-f0-9]*
    time = \d+\/\w+\/[\d|:|\s|\+]+
    method = \w{3,4}\b
    path = \/[\w\/]+\b
    code, size = \d+
    """

    ip_address = re.compile(
        r'([(?:\d{,3}\.?){4}|[a-f0-9]*).*\[(\d+\/\w+\/[\d|:|\s|\+]+)\]\s\"(\w{3,4}\b)\s(\/[\w\/]+\b)\sHTTP\/1\.1\"\s(\d+)\s(\d+)')
    return ip_address.findall(log_string)[0]


if __name__ == '__main__':

    with open(os.path.join('data', 'nginx_logs.txt')) as f:
        while True:
            line = f.readline()
            if not line:
                break
            else:
                print(parse_log_string(line))

    # ('80.91.33.133', '04/Jun/2015:07:06:16 +0000', 'GET', '/downloads/product_1', '304', '0')
    # ('144.76.151.58', '04/Jun/2015:07:06:05 +0000', 'GET', '/downloads/product_2', '304', '0')
    # ('79.136.114.202', '04/Jun/2015:07:06:35 +0000', 'GET', '/downloads/product_1', '404', '334')
