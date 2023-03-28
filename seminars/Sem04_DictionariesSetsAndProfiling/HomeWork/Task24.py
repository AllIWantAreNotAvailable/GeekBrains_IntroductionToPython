""" Задача №24:
В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке,
причем кусты высажены только по окружности. Таким образом, у каждого куста есть ровно
два соседних. Всего на грядке растет N кустов.

Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них
выросло различное число ягод – на i-ом кусте выросло Ai ягод.

В этом фермерском хозяйстве внедрена система автоматического сбора черники.
Эта система состоит из управляющего модулем и нескольких собирающих модулей.
Собирающий модуль за один заход, находясь непосредственно перед некоторым
кустом, собирает ягоды с этого куста и с двух соседних с ним.

Напишите программу для нахождения максимального числа ягод, которое может
собрать за один заход собирающий модуль, находясь перед некоторым кустом
заданной во входном файле грядки.

4 -> 1 2 3 4
9
"""
from random import randint


def get_max_of_triplets(*args) -> int:
    """ Функция возвращает максимальное целое значение суммы тройки переданных элементов.

    :param args: Элементы последовательности типа целое число.
    :return: Максимальное значение суммы трех элементов последовательности, <class 'int'>
    """
    length = len(args)
    sum_of_triplet = lambda bush: sum((args[bush - 2], args[bush - 1], args[bush]))
    berry_harvested = tuple(map(sum_of_triplet, range(length)))
    return max(berry_harvested)


# [ ] Добавить функционал ввода последовательностей пользователем.
def user_input():
    pass


def main():
    """ Главная функция.

    :return: None
    """
    bushes = [randint(1, 10) for _ in range(0, 4)]
    print(bushes, '->', get_max_of_triplets(*bushes))


if __name__ == '__main__':
    main()