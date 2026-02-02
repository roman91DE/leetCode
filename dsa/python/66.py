from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        return f(digits)


def f(digits: List[int]) -> List[int]:
    solution = []
    carry = False
    for i, num in enumerate(reversed(digits)):
        dig = num
        if i == 0 or carry:
            dig += 1
            carry = dig > 9
            dig = dig % 10
        solution.append(dig)
    if carry:
        solution.append(1)
    return list(reversed(solution))
