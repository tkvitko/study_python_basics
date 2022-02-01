def get_uniq_numbers(src: list) -> list:
    """Функция возвращает список элементов, которые имеются во входном списке в 1 экземпляре"""

    unique_numbers = [] # список для того, чтобы сохранить последовательность
    tmp = set()
    for el in src:
        if el not in tmp:
            unique_numbers.append(el)
        else:
            if el in unique_numbers:
                unique_numbers.remove(el)   # для списка это будет сложность O(n)
        tmp.add(el)
    return unique_numbers


src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print(*get_uniq_numbers(src))
