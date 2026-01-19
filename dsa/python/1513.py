from itertools import islice


class Solution:
    def numSub(self, s: str) -> int:
        return f(s)


def count_overlapping(s: str, substring: str) -> int:
    """Count overlapping occurrences using itertools sliding window"""
    sub_len = len(substring)
    if sub_len > len(s):
        return 0

    # Create sliding windows of substring length
    windows = zip(*(islice(s, i, None) for i in range(sub_len)))

    # Count how many windows match the substring
    return sum(1 for window in windows if "".join(window) == substring)


def f(s: str) -> int:

    acc = 0
    max_len = len(s)

    for i in range(1, max_len + 1):
        query = "1" * i
        acc += count_overlapping(s, query)

    return acc % (10**9 + 7)


def test_count_overlapping():
    assert count_overlapping("111", "11") == 2
    assert count_overlapping("1111", "11") == 3
    assert count_overlapping("0110111", "11") == 3


def test_1():
    s = "0110111"
    expected = 9
    assert f(s) == expected


def test_2():
    s = "101"
    expected = 2
    assert f(s) == expected


def test_3():
    s = "111111"
    expected = 21
    assert f(s) == expected