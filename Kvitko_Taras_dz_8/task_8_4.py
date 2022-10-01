from functools import wraps


def val_checker(val_check_func):
    def _val_checker(func):
        @wraps(func)
        def wrapper(*args):
            if args:
                for arg in args:
                    if not val_check_func(arg):
                        raise ValueError(f'wrong val {arg}')
            return func(*args)

        return wrapper

    return _val_checker


def validator(x):
    """Функция проверки переданного значения (положительное целое число или 0)"""
    if isinstance(x, int) and x >= 0:
        return True
    return False


@val_checker(validator)
def calc_cube(x):
    """Возведение числа в третью степень"""
    return x ** 3


if __name__ == '__main__':
    print(f'Имя декоратора замаскировано: {calc_cube.__name__}')
    print(calc_cube(5))
    print(calc_cube('ss'))
