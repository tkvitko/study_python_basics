import os
import sys

STRING_LENGTH = 7  # придется захардкодить длину строки, чтобы точно найти позицию

if len(sys.argv) < 3:
    print('Введите значение и номер строки')
    sys.exit(1)
else:
    with open(os.path.join('data', 'bakery.csv'), 'r+', encoding='utf-8') as f:
        script, amount, position = sys.argv
        position = int(position)
        lines_count = sum(1 for line in f)  # считаем количество строк в файле

        if position > lines_count:
            print('Нет такой строки')
        else:
            f.seek((position - 1) * STRING_LENGTH)  # ищем позицию, начиная с которой нужно записывать значение
            f.write(f'{amount.zfill(STRING_LENGTH - 1)}')  # "добиваем" значение нулями, чтобы длина строки сохранилась
