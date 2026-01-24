from typing import List


def minimumPairRemoval(nums: List[int]) -> int:
    return f(nums, 0)


def f(nums: List[int], acc: int = 0) -> int:
    for i, (fst, scnd) in enumerate(zip(nums, nums[1:], strict=False)):
        if fst > scnd:
            arr = nums[:i] + [fst + scnd] + nums[1 + 2 :]
            return f(arr, acc + 1)
    return acc


tst_case = [5, 2, 3, 1]
