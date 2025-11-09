class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        return f(num1, num2)


def rec(num1: int, num2: int) -> int:
    def inner(n1: int, n2: int, acc: int):
        if n1 == 0 or n2 == 0:
            return acc
        elif n1 >= n2:
            n1 -= n2
        else:
            n2 -= n1
        return inner(n1, n2, acc + 1)

    return inner(num1, num2, 0)


def it(num1: int, num2: int) -> int:
    c = 0

    while num1 != 0 and num2 != 0:
        c += 1
        if num1 >= num2:
            num1 -= num2
        else:
            num2 -= num1

    return c


f = it
