from functools import wraps


def type_logger(func):
    @wraps(func)
    def logger(*args, **kwargs):
        log = func(*args, **kwargs)

        print(f'{func.__name__}(', end='')

        if args:
            for arg in args:
                print(f'{arg}: {type(arg)}', end=', ')
        if kwargs:
            for key, value in kwargs.items():
                print(f'{key}: {type(value)}', end=', ')
        print(f'Result {log}: {type(log)})')

        return log

    return logger


@type_logger
def calc_cube(x, exp):
    return x ** exp


if __name__ == '__main__':
    a = calc_cube(x=5, exp=3)
    print(f'Имя декоратора замаскировано: {calc_cube.__name__}')
