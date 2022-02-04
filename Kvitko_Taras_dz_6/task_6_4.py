import os
import sys

USERS_FILE = os.path.join('data', 'users.csv')
HOBBIES_FILE = os.path.join('data', 'hobbi.csv')
USERS_HOBBIES_FILE = os.path.join('data', 'users_hobbies.txt')


def parse_files(users_file: str, hobbies_file: str, users_hobbies_file: str) -> None:
    with open(users_file, encoding='utf-8') as users_f:
        with open(hobbies_file, encoding='utf-8') as hobbies_f:
            with open(users_hobbies_file, 'w', encoding='utf-8') as users_hobbies_f:

                while True:
                    user = users_f.readline()
                    hobby = hobbies_f.readline()
                    if not hobby:
                        hobby = None
                        if not user:
                            break
                    else:
                        if not user:
                            sys.exit(1)
                    users_hobbies_f.write(f'{user.strip()}: {hobby}')


if __name__ == '__main__':
    parse_files(users_file=USERS_FILE, hobbies_file=HOBBIES_FILE, users_hobbies_file=USERS_HOBBIES_FILE)
