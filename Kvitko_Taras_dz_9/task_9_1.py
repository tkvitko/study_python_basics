from time import sleep


class TrafficLight:

    def __init__(self):
        """Светофор создается с красным светом по-умолчанию"""
        self.__color = 'red'

    def __switch_color(self, new_color: str, timeout: int):
        """
        Приватный метод смены цвета

        :param new_color: цвет, на который нужно переключиться
        :param timeout: время в секундах, через которое нужно переключиться
        :return: None

        """
        print(f'{self.__color} {timeout} сек')
        sleep(timeout)
        self.__color = new_color

    # методы класса
    def running(self, count=3):
        """
        Публичный метод запуска светофора

        :param count: количество переключений света, по умолчанию 3
        :return: None

        """
        while count:
            if self.__color == 'red':
                self.__switch_color(new_color='yellow', timeout=4)
            elif self.__color == 'yellow':
                self.__switch_color(new_color='green', timeout=2)
            elif self.__color == 'green':
                self.__switch_color(new_color='red', timeout=3)
            count -= 1


if __name__ == '__main__':
    traffic = TrafficLight()
    traffic.running(count=3)
