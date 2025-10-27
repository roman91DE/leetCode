from typing import List, NamedTuple


def _solveUneven(nums1: List[int], nums2: List[int], limit: int) -> float:
    for _ in range(limit):
        if nums1 and nums2:
            if nums1[0] < nums2[0]:
                nums1.pop(0)
            else:
                nums2.pop(0)
        elif nums1:
            nums1.pop(0)
        elif nums2:
            nums2.pop(0)
        else:
            raise RuntimeError("Should never happen")

    vals = []
    if nums1:
        vals.append(nums1.pop(0))
    if nums2:
        vals.append(nums2.pop(0))

    return float(min(vals))


def _solveEven(nums1: List[int], nums2: List[int], limit: int) -> float:
    for _ in range(limit - 1):
        if nums1 and nums2:
            if nums1[0] < nums2[0]:
                nums1.pop(0)
            else:
                nums2.pop(0)
        elif nums1:
            nums1.pop(0)
        elif nums2:
            nums2.pop(0)
        else:
            raise RuntimeError("Should never happen")

    final_vals = []

    while nums1 and nums2 and len(final_vals) < 2:
        if nums1[0] < nums2[0]:
            final_vals.append(nums1.pop(0))
        else:
            final_vals.append(nums2.pop(0))

    while nums1 and len(final_vals) < 2:
        final_vals.append(nums1.pop(0))

    while nums2 and len(final_vals) < 2:
        final_vals.append(nums2.pop(0))

    return (final_vals[0] + final_vals[1]) / 2


def findMedian(nums1: List[int], nums2: List[int]) -> float:
    n1, n2 = len(nums1), len(nums2)
    is_even = (n1 + n2) % 2 == 0
    if is_even:
        return _solveEven(nums1, nums2, (n1 + n2 + 1) // 2)
    else:
        return _solveUneven(nums1, nums2, (n1 + n2) // 2)


f = findMedian


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        return f(nums1, nums2)


class Testcase(NamedTuple):
    a: list[int]
    b: list[int]
    result: float


cases = [Testcase([1, 3], [2], 2.0), Testcase([1, 2], [3, 4], 2.5)]

for i, case in enumerate(cases):
    print(case)
    res = f(case.a, case.b)
    print(res == case.result)
