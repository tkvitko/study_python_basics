def get_digits_of_number(number: int) -> list:
    digits = []

    while number > 0:
        digit = number % 10
        digits.append(digit)
        number //= 10

    return digits


def sum_list(dataset: list) -> int:
    sum_ = 0
    for item in dataset:
        if sum(get_digits_of_number(item)) % 7 == 0:
            sum_ += item

    return sum_


def sum_list_2(dataset: list) -> int:
    sum_ = 0
    for item in dataset:

        # суммирование элементов после изменения
        item += 17
        if sum(get_digits_of_number(item)) % 7 == 0:
            sum_ += item

    return sum_


# создание списка
list_ = [x ** 3 for x in range(1, 1001) if x % 2 != 0]

print(sum_list(list_))
print(sum_list_2(list_))
