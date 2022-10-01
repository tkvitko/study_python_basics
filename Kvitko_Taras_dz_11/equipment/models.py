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
        self.summary: defaultdict = defaultdict(int)
        self.units: set = set()

    def __str__(self):
        return f'{self.name}: {self.summary.items()}'

    @check_objects(from_arg_number=2)
    def transit(self, other, object_):
        """Метод перемещения оборудования из одного места в другое"""
        if object_ in self.units:
            self.summary[object_.__class__.__name__] -= 1
            self.units.remove(object_)
            other.summary[object_.__class__.__name__] += 1
            other.units.add(object_)
        else:
            raise NotEnoughEquipment('No such equipment')

    @property
    def units_list(self):
        """Свойство, содержащий полные список имеющегося оборудования"""
        list_ = list()
        for unit in self.units:
            list_.append(unit.__dict__)
        return list_

    def search_unit(self, type_: str, property_: tuple):
        """Метод поиска оборудования по конкретным характеристикам"""
        for unit in self.units:
            if unit.__class__.__name__ == type_ and property_[0] in unit.__dict__:
                if unit.__dict__[property_[0]] == property_[1]:
                    return unit
        else:
            raise NotEnoughEquipment('No such equipment')

    def iter_units(self):
        """Метод, возвращающий генератор для итерирования по имеющемуся оборудованию"""
        for unit in self.units:
            yield unit


class Storage(Place):

    @check_objects(from_arg_number=1)
    def add(self, object_):
        """Метод для приемки оборудования на склад"""
        self.summary[object_.__class__.__name__] += 1
        self.units.add(object_)


class Office(Place):
    pass


class Equipment(ABC):
    def __init__(self, model: str):
        self.model: str = model

    def __str__(self):
        return f'{self.__class__.__name__} {self.model}'


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
