"""Задача 4:
Петя, Катя и Сережа делают из бумаги журавликов. Вместе
они сделали S журавликов. Сколько журавликов сделал каждый
ребенок, если известно, что Петя и Сережа сделали одинаковое
количество журавликов, а Катя сделала в два раза больше журавликов,
чем Петя и Сережа вместе?

Примеры:
-   6 -> 1 4 1
-   24 -> 4 16 4
-   60 -> 10 40 10
"""


def get_solution_crane_equation(cranes_count) -> tuple:
    """ Функция решает исключительно задачу №4, было выведено уравнение:

    y = x + 4x + x,

    где:

    - y - всего журавликов, которые сделали дети;
    - x - журавлики Пети (1-й операнд) и Серёжи (3-й операнд);
    - 4x – журавлики Кати (2-й операнд).
    В решении используем сокращенный вариант:

    x = y / 6

    :param cranes_count: Общее кол-во журавликов, которые сделали дети, <class 'int'>
    :return: Возвращает кортеж содержащий значения типа int (журавлики_Пети, журавлики_Кати, журавлики_Серёжи),
    <class 'tuple'>.
    """
    x = int(cranes_count / 6)
    return x, x * 4, x


def get_number_of_cranes_from_user(message='') -> int:
    """ Запрашиваем у пользователя количество сделанных детьми журавликов. Если пользователь ввел не только цифры,
    то вызывается рекуррентный случай.

    :param message: По умолчанию 'Пустая строка', принимает значение в рекуррентном вызове.
    :return: Количество журавликов, которое сделали дети, <class 'int'>.
    """
    cranes = input(f'{message}Сколько всего журавликов сделали дети?\n>>> ')
    return int(cranes) if cranes.isdigit() else get_number_of_cranes_from_user('Ошибка, повторите ввод! ')


def main() -> None:
    """ Главная функция.

    :return: None
    """
    cranes_count = get_number_of_cranes_from_user()
    if cranes_count % 6 != 0:
        print('Мы не умеем считать случае, которые выходят за условия задачи ;-(')
        return
    peter, kate, sergei = get_solution_crane_equation(cranes_count)
    print(f'Петя сделали {peter} журавликов, Сережа сделал столько же, сколько и Петя -> {sergei} журавликов,',
          f'а Катя -> {kate}')


if __name__ == '__main__':
    main()