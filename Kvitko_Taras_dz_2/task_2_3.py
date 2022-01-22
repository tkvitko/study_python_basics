import re


def convert_list_in_str_true_way(list_in: list) -> str:
    """
    ИМХО, только использование регулярки даст универсальное решение, где бы в элементе ни стояло число
    """

    str_out = ''

    for i in range(len(list_in)):

        digits = re.search(r'\d+', list_in[i])  # поиск цифр в элементе
        if digits:  # если в элементе нашлись цифры
            digits = digits.group(0)
            digits_with_zero = f'{int(digits):02d}'  # добавляем лидирующий ноль, если нужно
            new_value = re.sub(digits, digits_with_zero, list_in[i])  # меняем старый блок на новый с нулём
            str_out += f'"{new_value}" '  # записываем в строку значение в кавычках
        else:
            str_out += f'{list_in[i]} '  # если цифр нет, записываем в строку без кавычек

    return str_out


def convert_list_in_str_student_way(list_in: list) -> str:
    """
    Вариант без регулярок, рассчитанный только на случай, когда знак может быть перед числом
    """

    str_out = ''

    for i in range(len(my_list)):

        if my_list[i].isdigit():
            my_list[i] = '{0:02d}'.format(int(my_list[i]))
            str_out += f'"{my_list[i]}" '  # записываем в строку значение в кавычках
        elif my_list[i][1:].isdigit():
            sign = my_list[i][0]
            my_list[i] = '{1}{0:02d}'.format(abs(int(my_list[i])), sign)    # abs для исключения отрицательного int
            str_out += f'"{my_list[i]}" '  # записываем в строку значение в кавычках
        else:
            str_out += f'{my_list[i]} '  # если цифр нет, записываем в строку без кавычек

    return str_out


my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
result_1 = convert_list_in_str_true_way(my_list)
result_2 = convert_list_in_str_student_way(my_list)
print(result_1)
print(result_2)
