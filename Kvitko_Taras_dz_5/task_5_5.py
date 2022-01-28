src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
# result = [23, 1, 3, 10, 4, 11]

unique_numbers = []
tmp = set()
for el in src:
    if el not in tmp:
        unique_numbers.append(el)
    else:
        if el in unique_numbers:
            unique_numbers.remove(el)
    tmp.add(el)
print(unique_numbers)
