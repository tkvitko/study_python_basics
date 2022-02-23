class Complex:

    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __str__(self):
        return f'Число {self.real}+{self.imaginary}i'

    def __add__(self, other):
        return Complex(self.real + other.real, self.imaginary + other.imaginary)

    def __mul__(self, other):
        return Complex(self.real * other.real - self.imaginary * other.imaginary,
                       self.imaginary * other.real + self.real * other.imaginary)


if __name__ == '__main__':

    num_1 = Complex(1, 2)
    num_2 = Complex(3, 4)
    print(num_1 + num_2)
    print(num_1 * num_2)
