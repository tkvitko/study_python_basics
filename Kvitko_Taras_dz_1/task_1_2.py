def sum_list(dataset: list) -> int:
    sum_ = 0
    for item in dataset:

        # суммирование базовых элементов
        sum_of_digits = 0
        for digit in str(item):
            sum_of_digits += int(digit)
        if sum_of_digits % 7 == 0:
            sum_ += item

    return sum_


def sum_list_2(dataset: list) -> int:
    sum_ = 0
    for item in dataset:

        # суммирование элементов после изменения
        item += 17
        sum_of_digits = 0
        for digit in str(item):
            sum_of_digits += int(digit)
        if sum_of_digits % 7 == 0:
            sum_ += item

    return sum_


# создание списка
list_ = [x ** 3 for x in range(1, 1001) if x % 2 != 0]

print(sum_list(list_))
print(sum_list_2(list_))
