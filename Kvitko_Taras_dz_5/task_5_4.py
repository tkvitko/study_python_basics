
# решение с итератором
def get_number(source: list):
    for i in range(len(source) - 1):
        if source[i] < source[i + 1]:
            yield source[i + 1]


src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result = [el for el in get_number(src)]
print(result)
