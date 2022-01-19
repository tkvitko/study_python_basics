def convert_time(duration: int) -> str:
    # кортежи известных значений
    counts = (60, 60, 24)
    names = ['дн', 'час', 'мин', 'сек']
    results = []

    # заполнение значений
    for count in counts:
        result = duration % count
        results.append(result)
        duration //= count

    results.append(duration)

    # ислючение нулевых лидирующих позиций
    while results[-1] == 0:
        results.pop(-1)
        names.pop(0)

    # вывод результатов
    string_ = ''
    for value, name in zip(results[::-1], names):
        string_ += f'{value} {name} '

    return string_[:-1]  # убираем лишний пробел в конце


duration = 400153
# duration = 3615
print(convert_time(duration))
