strs = ["10", "0001", "111001", "1", "0"]
m = 5
n = 3
need = 4


# m zeros
# n ones


def f(strs: list[str], m: int, n: int) -> int:
    def count(l: list[str], symb: str) -> int:
        ct = 0
        for word in l:
            for c in word:
                if c == symb:
                    ct += 1
        return ct

    return 1


got = f(strs, m, n)
print(got == need)
