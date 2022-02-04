import sys

from task_6_4 import parse_files

if len(sys.argv) < 4:
    print('Введены не все параметры')
    sys.exit(1)
else:
    script, users_file, hobbies_file, out_file = sys.argv
    parse_files(users_file=users_file,
                hobbies_file=hobbies_file,
                users_hobbies_file=out_file)
