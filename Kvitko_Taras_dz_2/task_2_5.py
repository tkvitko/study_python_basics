def stringify(source_list: list) -> str:
    str_ = ''
    for item in source_list:
        nums_item = str(item).split('.')  # делим строку на рубли и копейки по точке
        rubles = nums_item[0]  # рубли это первый элемент списка
        try:
            cents = nums_item[1]  # копейки это второй элемент списка, если он есть
        except IndexError:
            cents = 0

        if len(str(cents)) < 2:  # добавляем ноль в начале, если копеек меньше 10
            cents = f'0{cents}'

        str_ += f'{rubles} руб {cents} коп, '

    return str_


if __name__ == '__main__':
    my_list = [57.8, 46.51, 97, 5.04, 7.0, 35.25, 76.7, 64.24, 5.6, 7.67]

    print('A. Вывод списка цен строкой:')
    print(stringify(my_list))

    print('\nB. Вывод отсортированного списка без создания нового:')
    print(id(my_list), my_list)
    my_list.sort()
    print(id(my_list), my_list)

    print('\nC. Новый список, содержащий те же цены, но отсортированные по убыванию:')
    new_list = sorted(my_list, reverse=True)
    print(id(new_list), new_list)

    print('\nD. Цены 5-ти самых дорогих товаров по возрастанию:')
    print(my_list[-5:])
