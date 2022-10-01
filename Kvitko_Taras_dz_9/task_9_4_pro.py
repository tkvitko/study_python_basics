class Car:
    is_police: bool = False

    def __init__(self, speed: int, color: str, name: str, is_police: bool):
        """
        Конструктор класса
        :param speed: текущая скорость автомобиля
        :param color: цвет автомобиля
        :param name: название марки автомобиля
        :param is_police: полицейский автомобиль или гражданский

        """
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self) -> None:
        """
        Увеличивает значение скорости на 15
        :return: в stdout сообщение по формату
            'Машина <название марки машины> повысила скорость на 15: <текущая скорость машины>'
        """
        step = 15
        self.speed += step
        print(f'Машина {self.name} повысила скорость на {step}: {self.speed}')

    def stop(self) -> None:
        """
        При вызове метода скорость становится равной '0'
        :return: в stdout сообщение по формату '<название марки машины>: остановилась'
        """
        self.speed = 0
        print(f'{self.name}: остановилась')

    def turn(self, direction: str) -> None:
        """
        Принимает направление движения автомобиля
        :param direction: строковое представление направления движения, может принимать только
            следующие значения: 'направо', 'налево', 'прямо', 'назад'
        :return: в stdout сообщение по формату
            '<название марки машины>: движется <direction>'
        """
        if direction in ['направо', 'налево', 'прямо', 'назад']:
            print(f'{self.name}({self.__class__.__name__}): движется {direction}')
        else:
            raise ValueError('нераспознанное направление движения')

    def show_speed(self) -> None:
        """
        Проверка текущей скорости автомобиля
        :return: в stdout выводит сообщение формата
            '<название марки машины>: текущая скорость <значение текущей скорости> км/час'
        """
        print(f'{self.name}: текущая скорость {self.speed} км/час')
        if self.is_police:
            print('Вруби мигалку и забудь про скорость!')

    def _show_speed_with_limit(self, speed_limit):
        if self.speed > speed_limit:
            print(f'Alarm!!! Speed!!!')
        else:
            print(f'{self.name}: текущая скорость {self.speed} км/час')


class TownCar(Car):

    def show_speed(self) -> None:
        super()._show_speed_with_limit(speed_limit=60)


class SportCar(Car):
    pass


class WorkCar(Car):

    def show_speed(self) -> None:
        super()._show_speed_with_limit(speed_limit=40)


class PoliceCar(Car):
    pass


if __name__ == '__main__':
    town_car = TownCar(41, "red", 'WW_Golf', is_police=False)
    work_car = WorkCar(41, 'yellow', 'BobCat', is_police=False)
    police_car = PoliceCar(120, "blue", 'BMW', is_police=True)
    sport_car = SportCar(300, 'white', 'Ferrari', is_police=False)
    town_car.go()  # Машина WW_Golf повысила скорость на 15: 56
    town_car.show_speed()  # WW_Golf: текущая скорость 56 км/час
    work_car.show_speed()  # Alarm!!! Speed!!!
    town_car.stop()  # WW_Golf: остановилась
    police_car.show_speed()
    # BMW: текущая скорость 120 км/час
    # Вруби мигалку и забудь про скорость!
    sport_car.turn('назад')  # Ferrari(SportCar): движется назад
    sport_car.turn('right')
    """
    Traceback (most recent call last):
      ...
    ValueError: нераспознанное направление движения
    """
