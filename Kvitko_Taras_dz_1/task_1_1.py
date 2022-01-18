def convert_time(duration: int) -> str:
    # кортежи известных значений
    counts = (60, 60, 24)
    names = ('дн', 'час', 'мин', 'сек')
    results = []

    # заполнение значений
    for count in counts:
        result = duration % count
        results.append(result)
        duration //= count

    results.append(duration)

    # вывод результатов
    string_ = ''
    for value, name in zip(results[::-1], names):
        if value:
            string_ += f'{value} {name} '

    return string_


duration = 400153
print(convert_time(duration))
