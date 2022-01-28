

def odd_nums(max_number: int):
    for number in range(1, max_number + 1, 2):
        yield number


if __name__ == '__main__':
    odd_to_15 = odd_nums(15)
    print(next(odd_to_15))
    print(next(odd_to_15))
    print(next(odd_to_15))
    print(next(odd_to_15))
    print(next(odd_to_15))
    print(next(odd_to_15))
    print(next(odd_to_15))
    print(next(odd_to_15))
    print(next(odd_to_15))
