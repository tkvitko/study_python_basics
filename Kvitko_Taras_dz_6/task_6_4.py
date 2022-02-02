import sys
from itertools import zip_longest


def parse_files(users_file='users.csv', hobbies_file='hobbi.csv', users_hobbies_file='users_hobbies.txt'):
    with open(users_file, encoding='utf-8') as users_f:
        with open(hobbies_file, encoding='utf-8') as hobbies_f:
            with open(users_hobbies_file, 'w', encoding='utf-8') as users_hobbies_f:

                for user, hobbi in zip_longest(users_f.readlines(), hobbies_f.readlines()):
                    if not user:
                        sys.exit(1)
                    else:
                        users_hobbies_f.write(f'{user.strip()}: {hobbi}')
