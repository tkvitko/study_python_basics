class Date:
    """

    Строковая дата.
    При инициализации объекта требует дату, переданную в формате ДД-ММ-ГГГГ

    """

    def __init__(self, date_string):
        self.date_string = date_string

    @classmethod
    def get_numbers(cls, date_string):
        """Парсит строку, возвращая список int"""
        return list(map(int, date_string.split('-')))

    @staticmethod
    def validate_string(numbers):
        """Валидирует переданные числа на предмет пригодности к формированию даты"""
        valid_ranges = [range(1, 31), range(1, 12), range(1970, 2999)]

        for value, range_ in zip(numbers, valid_ranges):
            if value not in range_:
                raise ValueError(f'wrong value {value}')
        else:
            return True


if __name__ == '__main__':
    print(Date.validate_string(Date.get_numbers('12-04-1986')))
    print(Date.validate_string(Date.get_numbers('12-13-1986')))
