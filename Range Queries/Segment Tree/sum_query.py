from math import ceil, log2


class SegmentTree:
    def __init__(self, A: list[int]) -> None:
        self.n = 2 ** ceil(log2(len(A)))
        self.tree = [0] * (self.n * 2)

        for k, x in enumerate(A):
            self.add(k, x)

    def add(self, k: int, x: int) -> None:
        k += self.n

        self.tree[k] += x
        k //= 2

        while k >= 1:
            self.tree[k] = self.tree[k * 2] + self.tree[k * 2 + 1]
            k //= 2

    def sum(self, a: int, b: int) -> int:
        a += self.n
        b += self.n

        s = 0

        while a <= b:
            if a % 2 == 1:
                s += self.tree[a]
                a += 1

            if b % 2 == 0:
                s += self.tree[b]
                b -= 1

            a //= 2
            b //= 2

        return s
