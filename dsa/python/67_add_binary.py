from typing import Tuple


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return badd(a, b)


def badd(fst: str, scnd: str) -> str:
    def f(a: str, b: str, carry: bool) -> Tuple[str, bool]:
        t = int(a) + int(b) if not carry else int(a) + int(b) + 1
        new_carry = t > 1
        if new_carry:
            t -= 2
        return (str(t), new_carry)

    max_length = max(len(fst), len(scnd))

    fst = fst.zfill(max_length)
    scnd = scnd.zfill(max_length)

    carry = False
    buf = []

    for _f, _s in zip(reversed(fst), reversed(scnd), strict=True):
        temp, carry = f(_f, _s, carry)
        buf.append(temp)

    if carry:
        buf.append("1")
    return "".join(reversed(buf))
