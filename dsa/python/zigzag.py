from itertools import chain


def zigzag(s: str, numRows: int) -> str:
    if numRows == 1:
        return s
    length = len(s)
    rows = [["" for _ in range(length)] for _ in range(numRows)]
    diagonal = numRows - 2
    chars = list(s)

    while chars:
        for r in range(numRows):
            if chars:
                rows[r].append(chars.pop(0))
            else:
                break
        for d in range(diagonal):
            if chars:
                for r in range(numRows - 2, 0, -1):
                    if chars:
                        for _ in range(numRows - 2 - d):
                            rows[r].append("")
                        rows[r].append(chars.pop(0))
                    else:
                        break
            else:
                break

    return "".join(chain(*rows))
