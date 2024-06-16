from math import inf, ceil, log2


class SegmentTree:
    def __init__(self, A: list[int]) -> None:
        self.n = 2 ** ceil(log2(len(A)))
        self.tree = [inf] * (self.n * 2)

        for k, x in enumerate(A):
            self.set(k, x)

    def set(self, k: int, x: int) -> None:
        k += self.n

        self.tree[k] = x
        k //= 2

        while k >= 1:
            self.tree[k] = min(self.tree[k * 2], self.tree[k * 2 + 1])
            k //= 2

    def min(self, a: int, b: int) -> int:
        a += self.n
        b += self.n

        res = inf

        while a <= b:
            if a % 2 == 1:
                res = min(res, self.tree[a])
                a += 1

            if b % 2 == 0:
                res = min(res, self.tree[b])
                b -= 1

            a //= 2
            b //= 2

        return res
    
    def min_index(self) -> int:
        k = 1

        while k * 2 < len(self.tree):
            if self.tree[k] == self.tree[k * 2]:
                k = k * 2
            else:
                k = k * 2 + 1

        return k - self.n
