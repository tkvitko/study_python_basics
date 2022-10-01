from typing import List


class Matrix:
    """Класс Матрица"""

    def __init__(self, matrix: List[List[int]]):
        """Инициализация матрицы из списка списков"""
        for row_number in range(1, len(matrix)):
            # Если найдем хотя бы одну строку с длиной, отличной от предыдущей, бракуем вход
            if len(matrix[row_number]) != len(matrix[row_number - 1]):
                raise ValueError('fail initialization matrix')
        else:
            self.matrix = matrix

    def __str__(self):
        """Вывод матрицы в привычном виде"""
        return '\n'.join([f'| {" ".join([str(el) for el in row])} |' for row in self.matrix])

    def __add__(self, other):
        """Сложение матриц по правилу сложения матриц"""
        if len(self.matrix) != len(other.matrix) or \
                len(self.matrix[0]) != len(other.matrix[0]):
            # сложить можно только матрицы одного размера
            raise ValueError('cant add matrix')
        else:
            new = [[self.matrix[i][j] + other.matrix[i][j] for j in range(len(self.matrix[0]))] for i in
                   range(len(self.matrix))]
            return Matrix(new)


if __name__ == '__main__':
    first_matrix = Matrix([[1, 2], [3, 4], [5, 6]])
    second_matrix = Matrix([[6, 5], [4, 3], [2, 1]])
    print(first_matrix)
    """
    | 1 2 |
    | 3 4 |
    | 5 6 |
    """
    print(first_matrix + second_matrix)
    """
    | 7 7 |
    | 7 7 |
    | 7 7 |
    """
    fail_matrix = Matrix([[1, 2], [3, 4, 7], [5, 6]])
    """
    Traceback (most recent call last):
      ...
    ValueError: fail initialization matrix
    """
