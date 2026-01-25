from itertools import chain

"""
313
a e
bdf
c g

4114
a  g
b fh
ce i
d  j

51115
a   i
b  hj
c g k
df  l
e   m

"""


def zigzag(s: str, numRows: int) -> str:
    if numRows == 1:
        return s
    length = len(s)
    rows = [["" for _ in range(length)] for _ in range(numRows)]

    return "".join(chain(*rows))
