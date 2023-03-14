"""
У вас есть девять цифр: 1, 2, …, 9. Именно в таком порядке. Вы можете вставлять между ними знаки «+»,
«-» или ничего. У вас будут получаться выражения вида 123+45-6+7+89. Найдите все из них, которые равны 100.

=====================
Группы (варианты группировки):
1) 9 групп по 1 члену:
    1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9

2) 8 групп по 2 и 1 члену:
    12 | 3 | 4 | 5 | 6 | 7 | 8 | 9
    1 | 23 | 4 | 5 | 6 | 7 | 8 | 9
    1 | 2 | 34 | 5 | 6 | 7 | 8 | 9
    1 | 2 | 3 | 45 | 6 | 7 | 8 | 9
    1 | 2 | 3 | 4 | 56 | 7 | 8 | 9
    1 | 2 | 3 | 4 | 5 | 67 | 8 | 9
    1 | 2 | 3 | 4 | 5 | 6 | 78 | 9
    1 | 2 | 3 | 4 | 5 | 6 | 7 | 89

3) 7 групп по 3 и 1 члену:
    123 | 4 | 5 | 6 | 7 | 8 | 9
    1 | 234 | 5 | 6 | 7 | 8 | 9
    1 | 2 | 345 | 6 | 7 | 8 | 9
    1 | 2 | 3 | 456 | 7 | 8 | 9
    1 | 2 | 3 | 4 | 567 | 8 | 9
    1 | 2 | 3 | 4 | 5 | 678 | 9
    1 | 2 | 3 | 4 | 5 | 6 | 789

4) 7 групп по 2 и 1 члену:
    12 | 34 | 5 | 6 | 7 | 8 | 9
    12 | 3 | 45 | 6 | 7 | 8 | 9
    12 | 3 | 4 | 56 | 7 | 8 | 9
    12 | 3 | 4 | 5 | 67 | 8 | 9
    12 | 3 | 4 | 5 | 6 | 78 | 9
    12 | 3 | 4 | 5 | 6 | 7 | 89
    1 | 23 | 45 | 6 | 7 | 8 | 9
    1 | 23 | 4 | 56 | 7 | 8 | 9
    1 | 23 | 4 | 5 | 67 | 8 | 9
    1 | 23 | 4 | 5 | 6 | 78 | 9
    1 | 23 | 4 | 5 | 6 | 7 | 89
    1 | 2 | 34 | 56 | 7 | 8 | 9
    1 | 2 | 34 | 5 | 67 | 8 | 9
    1 | 2 | 34 | 5 | 6 | 78 | 9
    1 | 2 | 34 | 5 | 6 | 7 | 89
    1 | 2 | 3 | 45 | 67 | 8 | 9
    1 | 2 | 3 | 45 | 6 | 78 | 9
    1 | 2 | 3 | 45 | 6 | 7 | 89
    1 | 2 | 3 | 4 | 56 | 78 | 9
    1 | 2 | 3 | 4 | 56 | 7 | 89
    1 | 2 | 3 | 4 | 5 | 67 | 89

5) 6 групп по 4 и 1 члену:
    1234 | 5 | 6 | 7 | 8 | 9
    1 | 2345 | 6 | 7 | 8 | 9
    1 | 2 | 3456 | 7 | 8 | 9
    1 | 2 | 3 | 4567 | 8 | 9
    1 | 2 | 3 | 4 | 5678 | 9
    1 | 2 | 3 | 4 | 5 | 6789

6) 6 групп по 3, 2 и 1 члену:
    123 | 45 | 6 | 7 | 8 | 9
    123 | 4 | 56 | 7 | 8 | 9
    123 | 4 | 5 | 67 | 8 | 9
    123 | 4 | 5 | 6 | 78 | 9
    123 | 4 | 5 | 6 | 7 | 89
    1 | 234 | 56 | 7 | 8 | 9
    1 | 234 | 5 | 67 | 8 | 9
    1 | 234 | 5 | 6 | 78 | 9
    1 | 234 | 5 | 6 | 7 | 89
    1 | 2 | 345 | 67 | 8 | 9
    1 | 2 | 345 | 6 | 78 | 9
    1 | 2 | 345 | 6 | 7 | 89
    1 | 2 | 3 | 456 | 78 | 9
    1 | 2 | 3 | 456 | 7 | 89
    1 | 2 | 3 | 4 | 567 | 89
    1 | 2 | 3 | 4 | 56 | 789
    1 | 2 | 3 | 45 | 6 | 789
    1 | 2 | 34 | 5 | 6 | 789
    1 | 23 | 4 | 5 | 6 | 789
    12 | 3 | 4 | 5 | 6 | 789
    1 | 2 | 3 | 45 | 678 | 9
    1 | 2 | 34 | 5 | 678 | 9
    1 | 23 | 4 | 5 | 678 | 9
    12 | 3 | 4 | 5 | 678 | 9
    1 | 2 | 34 | 567 | 8 | 9
    1 | 23 | 4 | 567 | 8 | 9
    12 | 3 | 4 | 567 | 8 | 9
    1 | 23 | 456 | 7 | 8 | 9
    12 | 3 | 456 | 7 | 8 | 9
    12 | 345 | 6 | 7 | 8 | 9

7) 6 групп по 2 и 1 члену:
    12 | 34 | 56 | 7 | 8 | 9
    12 | 34 | 5 | 67 | 8 | 9
    12 | 34 | 5 | 6 | 78 | 9
    12 | 34 | 5 | 6 | 7 | 89
    12 | 3 | 45 | 67 | 8 | 9
    12 | 3 | 45 | 6 | 78 | 9
    12 | 3 | 45 | 6 | 7 | 89
    12 | 3 | 4 | 56 | 78 | 9
    12 | 3 | 4 | 56 | 7 | 89
    12 | 3 | 4 | 5 | 67 | 89

    1 | 23 | 45 | 67 | 8 | 9

# остановился на переборе 3-х 2-ных + 1-ничных групп, перебрал все случаи, где 1-я 2-ная группа начинается
# с 1-й позиции, записал начало первого сдвига крайней левой 2-ой группы.
"""