"""Задача №23:
Дан массив, состоящий из целых чисел. Напишите программу, которая подсчитает количество элементов массива, больших
предыдущего (элемента с предыдущим номером).

Input:
-   [0, -1, 5, 2, 3]
Output:
-   2 (-1 < 5, 2 < 3)

Примечание: Пользователь может вводить значения списка или список задан изначально.
"""

array = [0, -1, 5, 2, 3]
counter_list = [1 for x in range(1, len(array)) if array[x - 1] < array[x]]
print(f'В массиве:\n{array} -> {sum(counter_list)} элемента больше предыдущего.')
