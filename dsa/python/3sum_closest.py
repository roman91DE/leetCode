from copy import deepcopy
from typing import List, Optional
from math import inf
from itertools import combinations


def find_closest(nums: List[int], target: int) -> int:
    assert nums, "Array must not be empty"
    pos = 0
    diff = inf
    for i, num in enumerate(nums):
        delta = abs(num - target)
        if delta < diff:
            diff = delta
            pos = i
    return nums[pos]


def solve(nums: List[int], target: int) -> Optional[int]:
    combs = combinations(nums, 2)
    best_dif = inf
    best_sol = None
    for combination in combs:
        have = sum(combination)
        need = target - have
        arr = deepcopy(nums)
        arr.remove(combination[0])
        arr.remove(combination[1])
        best_pick = find_closest(arr, need)
        res = have + best_pick
        diff = target - res
        if diff < best_dif:
            best_dif = diff
            best_sol = res
    return best_sol


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        return solve(nums, target)  # type: ignore


""" 
nums = [10,20,30,40,50,60,70,80,90]
target = 1

Output -> 180
Correct -> 60

"""
