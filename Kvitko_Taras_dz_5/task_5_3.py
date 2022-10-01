import typing
from itertools import zip_longest

tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
classes = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']


def check_gen(tutors: list, classes: list) -> typing.Generator:
    """ Функция возвращает генератор, созданный на основе двух списков """

    return ((tutor, klass) for tutor, klass in zip_longest(tutors, classes) if tutor)


generator = check_gen(tutors, classes)
# добавьте здесь доказательство, что создали именно генератор
print(type(generator))

for _ in range(len(tutors)):
    print(next(generator))
next(generator)  # если раскомментировать, то должно падать в traceback по StopIteration
