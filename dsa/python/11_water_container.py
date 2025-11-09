from typing import List, NamedTuple
from itertools import permutations


class Entry(NamedTuple):
    position: int
    height: int


class Solution:
    def maxArea(self, height: List[int]) -> int:
        return f(height)


# @lru_cache(maxsize=None)
def compute_max(left: Entry, right: Entry) -> int:
    min_height = min(left.height, right.height)
    distance = right.position - left.position
    return min_height * distance


def naive(height: List[int]) -> int:
    entries = [Entry(i, n) for i, n in enumerate(height)]
    all_combination = permutations(entries, r=2)
    valid_combinations = [
        (a, b) for (a, b) in all_combination if a.position <= b.position
    ]

    best = 0

    for fst, scnd in valid_combinations:
        temp = compute_max(fst, scnd)
        if temp > best:
            best = temp

    return best


class PointerPair(NamedTuple):
    left: int
    right: int


def two_pointer(height: List[int]) -> int:
    def compute_volume(p: PointerPair) -> int:
        a = p.right - p.left
        b = min(height[p.left], height[p.right])
        return max(0, a * b)

    p = PointerPair(0, len(height) - 1)
    scores: list[int] = []

    while p.left < p.right:
        scores.append(compute_volume(p))

        if height[p.left] < height[p.right]:
            p = PointerPair(p.left + 1, p.right)
        else:
            p = PointerPair(p.left, p.right - 1)

    return max(scores)


f = two_pointer


height = [1, 8, 6, 2, 5, 4, 8, 3, 7]

res = f(height)
print(res == 49)

"""
python dsa/python/11_water_container.py 
"""
