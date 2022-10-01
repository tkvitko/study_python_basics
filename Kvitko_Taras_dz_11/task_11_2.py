class MyZeroException(Exception):

    def __init__(self, message):
        self.message = message


class MyNumber:

    def __init__(self, number):
        self.number = number

    def __truediv__(self, other):
        if other.number == 0:
            raise MyZeroException('так нельзя')
        else:
            return self.number / other.number


if __name__ == '__main__':
    x = MyNumber(10)
    y = MyNumber(0)
    print(x / y)
