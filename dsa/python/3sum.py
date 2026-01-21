from typing import List, Tuple


def three_sum(nums: List[int]) -> List[List[int]]:
    all_zero = all(map(lambda x: x == 0, nums))
    if all_zero:
        return [[0, 0, 0]] if len(nums) >= 3 else []

    def _two_sum(nums: List[int], target: int) -> List[List[int]]:
        i, j = 0, len(nums) - 1
        solutions = []
        while i < j:
            _temp = nums[i] + nums[j]
            if _temp == target:
                solutions.append([nums[i], nums[j]])
                i += 1
                j -= 1
            elif _temp < target:
                i += 1
            else:
                j -= 1
        return solutions

    snums = sorted(nums)
    buffer: set[Tuple[int]] = set()
    for i, num in enumerate(snums):
        arr = snums[:i] + snums[i + 1 :]
        sols = [tuple(sorted([num, *rest])) for rest in _two_sum(arr, -num)]
        for s in sols:
            buffer.add(s)  # type: ignore
    return [[*t] for t in buffer]


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return three_sum(nums)
