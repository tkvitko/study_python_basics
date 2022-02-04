import os

from pprint import pprint


def get_parse_attrs(line: str) -> tuple:
    """Парсит строку на атрибуты и возвращает кортеж атрибутов (<remote_addr>, <request_type>, <requested_resource>)"""
    line = line.strip()

    ip_address = line.split(' ')[0]
    other_props = line.split('"')[1]
    other_props_list = other_props.split(' ')
    http_method = other_props_list[0]
    request_path = other_props_list[1]

    return ip_address, http_method, request_path


list_out = list()
with open(os.path.join('data', 'nginx_logs.txt'), 'r', encoding='utf-8') as fr:
    for line_ in fr.readlines():
        result = get_parse_attrs(line_)
        list_out.append(result)

pprint(list_out)
