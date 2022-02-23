from abc import ABC
from collections import defaultdict

from .exceptions import NotEnoughEquipment, NotEquipment


def check_objects(from_arg_number):
    """
    Функция проверки, что агрументы, начиная с аргумента под номером from_arg_number, являются оборудованием
    """

    def check_objects_(method):
        def wrapper(*args):
            for arg in args[from_arg_number:]:
                if not issubclass(arg.__class__, Equipment):
                    raise NotEquipment('This is not equipment')
            else:
                return method(*args)

        return wrapper

    return check_objects_


class Place:

    def __init__(self, name):
        self.name: str = name
        self.units: defaultdict = defaultdict(int)

    def __str__(self):
        return f'{self.name}: {[(str(item[0]), item[1]) for item in self.units.items()]}'

    @check_objects(from_arg_number=1)
    def add(self, object_):
        self.units[object_] += 1

    @check_objects(from_arg_number=2)
    def transit(self, other, object_):
        if self.units[object_]:
            self.units[object_] -= 1
            other.units[object_] += 1
        else:
            raise NotEnoughEquipment('No such equipment')


class Storage(Place):
    pass


class Office(Place):
    pass


class Equipment(ABC):
    def __init__(self, model: str):
        self.model: str = model

    def __str__(self):
        return self.model


class Printer(Equipment):
    def __init__(self, model: str, is_colorful: bool):
        super().__init__(model)
        self.colorful: bool = is_colorful


class Scanner(Equipment):
    def __init__(self, model: str, resolution: tuple):
        super().__init__(model)
        for value in resolution:
            if isinstance(value, int):
                self.resolution: tuple = resolution
            else:
                raise TypeError


class Copier(Equipment):
    def __init__(self, model: str, speed: int):
        super().__init__(model)
        self.speed: int = speed
