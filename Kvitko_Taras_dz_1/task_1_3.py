def transform_string(number: int) -> str:
    if number % 10 == 1:  # если число оканчивается на 1
        if number != 11:
            word = 'процент'
        else:  # исключение - 11
            word = 'процентов'

    elif 2 <= number % 10 <= 4:  # если число оканчивается на 2, 3, 4
        if number // 10 == 1:  # исключение - второй десяток
            word = 'процентов'
        else:
            word = 'процента'

    else:  # остальные варианты
        word = 'процентов'

    return f'{number} {word}'


for n in range(1, 101):
    print(transform_string(n))
