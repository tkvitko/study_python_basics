from random import uniform


def transfer_list_in_str(list_in: list) -> str:
    """Преобразует каждый элемент списка (вещественное число) в строку вида '<r> руб <kk> коп' и
        формирует из них единую строковую переменную разделяя значения запятой."""

    str_out = ''
    for item in list_in:
        nums_item = str(item).split('.')  # делим строку на рубли и копейки по точке
        rubles = nums_item[0]  # рубли это первый элемент списка
        try:
            cents = nums_item[1]  # копейки это второй элемент списка, если он есть
        except IndexError:
            cents = 0

        if len(str(cents)) < 2:  # добавляем ноль в конце, если значение меньше 10
            cents = f'{cents}0'

        str_out += f'{rubles} руб {cents} коп, '

    return str_out[:-2]  # обрежем лишние ', '


my_list = [round(uniform(10, 100), 2) for _ in range(1, 16)]  # автоматическая генерация случайных 15 чисел
print(f'Исходный список: {my_list}')
result_1 = transfer_list_in_str(my_list)
print(result_1)


def sort_prices(list_in: list):
    """Сортирует вещественные числа по возрастанию, не создавая нового списка"""

    list_in.sort()
    return list_in


# зафиксируйте здесь информацию по исходному списку my_list
id_before_sorting = id(my_list)
result_2 = sort_prices(my_list)
# зафиксируйте здесь доказательство, что результат result_2 остался тем же объектом
print(result_2)
id_after_sorting = id(result_2)
print(f'{id_before_sorting} = {id_after_sorting}')


def sort_price_adv(list_in: list) -> list:
    """Создаёт новый список и возвращает список с элементами по убыванию"""
    return sorted(list_in, reverse=True)


result_3 = sort_price_adv(my_list)
print(result_3)
id_after_sorting = id(result_3)
print(f'{id_before_sorting} != {id_after_sorting}')


def check_five_max_elements(list_in: list) -> list:
    """Проверяет элементы входного списка вещественных чисел и возвращает
        список из ПЯТИ максимальных значений"""

    list_out = sorted(list_in)[-5:]
    return list_out


result_4 = check_five_max_elements(my_list)
print(result_4)
