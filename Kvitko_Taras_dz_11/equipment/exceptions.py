class NotEquipment(Exception):
    """Исключение о том, что данный объект не является объектом класса-потомка Equipment"""

    def __init__(self, message):
        self.message = message


class NotEnoughEquipment(Exception):
    """Исключение о том, что в месте-источнике нет такого Equipment"""

    def __init__(self, message):
        self.message = message
