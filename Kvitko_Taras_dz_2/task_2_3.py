import re

my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
str_ = ''

for i in range(len(my_list.copy())):

    digits = re.search(r'\d+', my_list[i])  # поиск цифр в элементе
    if digits:  # если в элементе нашлись цифры
        digits = digits.group(0)
        # digits_with_zero = f'0{digits}' if len(digits) < 2 else digits  # добавляем лидирующий ноль
        digits_with_zero = f'{int(digits):02d}'  # добавляем лидирующий ноль - более красивый вариант
        new_value = re.sub(digits, digits_with_zero, my_list[i])  # меняем старый блок на новый с нулём
        str_ += f'"{new_value}" '  # записываем в строку значение в кавычках
    else:
        str_ += f'{my_list[i]} '  # если цифр нет, записываем в строку без кавычек

print(str_)
