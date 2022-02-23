class NotANumber(Exception):

    def __init__(self, message):
        self.message = message


def check_if_number(string):
    try:
        return float(string)
    except ValueError:
        raise NotANumber('это не число')


if __name__ == '__main__':
    
    list_: list = list()
    stop_string = 'stop'

    while True:
        current_value = input(f'Введите число или {stop_string}, чтобы завершить: ')
        if current_value == stop_string:
            break
        else:
            try:
                float_ = check_if_number(current_value)
            except NotANumber:
                print('Это не число, в список не добавится')
            else:
                list_.append(float_)

    print(list_)
