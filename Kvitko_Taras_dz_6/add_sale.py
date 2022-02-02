import sys

if len(sys.argv) < 2:
    print('Введите значение')
    sys.exit(1)
else:
    with open('bakery.csv', 'a', encoding='utf-8') as f:
        script, amount = sys.argv
        f.write(f'{amount}\n')
