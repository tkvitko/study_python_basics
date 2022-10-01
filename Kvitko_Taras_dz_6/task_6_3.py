import json
import os
import sys
from itertools import zip_longest

USERS_FILE = os.path.join('data', 'users.csv')
HOBBIES_FILE = os.path.join('data', 'hobbi.csv')
USERS_HOBBIES_FILE = os.path.join('data', 'users_hobbies.json')


def prepare_dataset(path_users_file: str, path_hobby_file: str) -> dict:
    """
    Считывает данные из файлов и возвращает словарь, где:
        ключ — ФИО, значение — данные о хобби (список строковых переменных)
    :param path_users_file: путь до файла, содержащий ФИО пользователей, разделенных запятой по строке
    :param path_hobby_file: путь до файла, содержащий хобби, разделенные запятой по строке
    :return: Dict(str: Union[List[str]|None])
    """

    with open(path_users_file, encoding='utf-8') as users_f:
        users_data = users_f.read()  # память не экономим, потому для скорости забираем сразу всё
        users = users_data.splitlines()
        users = list(map(lambda s: s.replace(',', ' ').title(), users))

    with open(path_hobby_file, encoding='utf-8') as hobbies_f:
        hobbies_data = hobbies_f.read()
        hobbies = hobbies_data.splitlines()
        hobbies = list(map(lambda s: s.split(','), hobbies))

    if len(users) < len(hobbies):
        sys.exit(1)
    else:
        users_hobbies = {key: value for key, value in zip_longest(users, hobbies)}

    return users_hobbies


dict_out = prepare_dataset(USERS_FILE, HOBBIES_FILE)
with open(USERS_HOBBIES_FILE, 'w', encoding='utf-8') as fw:
    json.dump(dict_out, fw, ensure_ascii=False, indent=2)
