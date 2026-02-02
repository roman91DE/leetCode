from typing import List


def _minimumCost(nums):
    base = nums[0]
    rest = sorted(nums[1:])
    return sum(rest[:2]) + base


class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        return _minimumCost(nums)


nums1 = [1, 2, 3, 12]  # 6
nums2 = [5, 4, 3]  # 12
nums3 = [10, 3, 1, 1]  # 12
