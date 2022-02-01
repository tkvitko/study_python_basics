n = 15
odd_nums = (number for number in range(n + 1) if number % 2 == 1)

for _ in range(1, n + 1, 2):
    print(next(odd_nums))
next(odd_nums)  # если раскомментировать, то должно падать в traceback по StopIteration
