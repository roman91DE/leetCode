from typing import List


# def f(xs: List[int]) -> List[List[int]]:
#    nums = sorted(xs)
#    distances: List[int] = [nums[i] - nums[i - 1] for i in range(1, len(nums))]
#    min_mad: int = min(distances)
#    return [nums[i : i + 2] for i, dist in enumerate(distances) if dist == min_mad]


def f(xs: List[int]) -> List[List[int]]:
    nums = sorted(xs)
    distances: List[int] = [nums[i] - nums[i - 1] for i in range(1, len(nums))]
    min_mad: int = min(distances)
    pairs: List[List[int]] = []
    for i, dist in enumerate(distances):
        if dist == min_mad:
            pairs.append(nums[i : i + 2])
    return pairs


class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        return f(arr)
