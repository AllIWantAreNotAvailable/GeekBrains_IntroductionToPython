"""
Дано натуральное число n>1. Выведите все простые множители этого числа в порядке
не убывания с учетом кратности. Алгоритм должен иметь сложность O(logn).
"""


def wer(n):
    for i in range(2, n+1):
        if n%i == 0:
            if i == n:
                return [i]
            else:
                return [i] + wer(n//i)


print(wer(132_123_312_132_123))