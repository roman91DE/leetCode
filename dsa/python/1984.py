from collections.abc import Sequence
from typing import List, TypeVar

a = TypeVar("a")


def minimumDifference(nums: List[int], k: int) -> int:
    nums.sort()
    opts: List[int] = [fitness(lst) for lst in sliding_windows(nums, k)]
    return min(opts)


def sliding_windows(xs: Sequence[a], n: int) -> List[Sequence[a]]:
    return [xs[i : i + n] for i in range(0, len(xs) - (n - 1))]


def fitness(nums: Sequence[int]) -> int:
    return nums[-1] - nums[0]


class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        return minimumDifference(nums, k)
