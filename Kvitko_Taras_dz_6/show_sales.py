import os
import sys

mode = len(sys.argv)    # "режим работы" в зависимости от количества введенных параметров
with open(os.path.join('data', 'bakery.csv'), encoding='utf-8') as f:
    if mode == 1:  # полный список
        for line in f.readlines():
            print(line.strip())

    elif mode == 2:  # список, начиная с минимума
        script, min_number = sys.argv
        for line in f.readlines()[int(min_number) - 1:]:
            print(line.strip())

    elif mode == 3:  # список от минимума до максимума
        script, min_number, max_number = sys.argv
        for line in f.readlines()[int(min_number) - 1:int(max_number)]:
            print(line.strip())
