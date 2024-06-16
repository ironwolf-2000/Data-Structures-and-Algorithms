class FenwickTree:
    def __init__(self, A: list[int]) -> None:
        self.n = len(A)
        self.tree = [0] * (self.n + 1)

        for k in range(1, self.n + 1):
            self.add(k, A[k - 1])

    def add(self, k: int, x: int) -> None:
        while k <= self.n:
            self.tree[k] += x
            k += k & -k

    def sum(self, k: int) -> int:
        s = 0

        while k >= 1:
            s += self.tree[k]
            k -= k & -k

        return s

    def range_sum(self, a: int, b: int) -> int:
        return self.sum(b) - self.sum(a - 1)
