from abc import ABC, abstractmethod


class Clothes(ABC):
    """Абстрактный класс одежда"""

    def __init__(self, prop):
        if not isinstance(prop, float):
            raise ValueError('Value must be float')
        else:
            self._property = prop

    @abstractmethod
    def calculate(self):
        pass


class Coat(Clothes):

    @property
    def calculate(self):
        return round((self._property / 6.5 + 0.5), 2)


class Costume(Clothes):

    @property
    def calculate(self):
        return round((2 * self._property + 0.3), 2)


if __name__ == '__main__':
    coat = Coat(45.0)
    costume = Costume(3.0)

    print(coat.calculate)  # 7.42
    print(costume.calculate)  # 6.3
