import json
import sys
from itertools import zip_longest

USERS_FILE = 'users.csv'
HOBBIES_FILE = 'hobbi.csv'
USERS_HOBBIES_FILE = 'users_hobbies.json'

with open(USERS_FILE, encoding='utf-8') as users_f:
    with open(HOBBIES_FILE, encoding='utf-8') as hobbies_f:
        users_data = users_f.read()  # память не экономим, потому для скорости забираем сразу всё
        users = users_data.splitlines()
        users = list(map(lambda s: s.replace(',', ' '), users))

        hobbies_data = hobbies_f.read()
        hobbies = hobbies_data.splitlines()
        hobbies = list(map(lambda s: s.replace(',', ', '), hobbies))

if len(users) < len(hobbies):
    sys.exit(1)
else:
    users_hobbies = {key: value for key, value in zip_longest(users, hobbies)}

with open(USERS_HOBBIES_FILE, 'w', encoding='utf-8') as users_hobbies_f:
    json.dump(users_hobbies, users_hobbies_f)

with open(USERS_HOBBIES_FILE, encoding='utf-8') as users_hobbies_f:
    users_hobbies_read = json.load(users_hobbies_f)
    print(users_hobbies_read)
