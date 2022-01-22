def transform_string(number: int) -> str:
    if number % 10 == 1 and number != 11:
        word = 'процент'
    elif 2 <= number % 10 <= 4 and number // 10 != 1:
        word = 'процента'
    else:
        word = 'процентов'

    return f'{number} {word}'


for n in range(1, 101):
    print(transform_string(n))
