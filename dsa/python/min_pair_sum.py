from typing import List


def min_pair_sum(nums: List[int]) -> int:
    n = len(nums)
    mid = n // 2
    xs = sorted(nums)
    pair_sums = [(xs[i] + xs[(-i) - 1]) for i in range(mid)]
    return max(pair_sums)
