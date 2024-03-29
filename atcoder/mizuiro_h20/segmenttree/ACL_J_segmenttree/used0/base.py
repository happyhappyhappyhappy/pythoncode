import sys

class SegTree:
    def __init__(self, op, e, n, v=None):
        self._n = n
        self._op = op
        self._e = e
        self._log = (n - 1).bit_length()
        self._size = 1 << self._log
        self._d = [self._e()] * (self._size << 1)
        if v is not None:
            for i in range(self._n):
                self._d[self._size + i] = v[i]
            for i in range(self._size - 1, 0, -1):
                self._d[i] = self._op(self._d[i << 1], self._d[i << 1 | 1])

    def set(self, p, x):
        p += self._size
        self._d[p] = x
        while p:
            self._d[p >> 1] = self._op(self._d[p], self._d[p ^ 1])
            p >>= 1

    def get(self, p):
        return self._d[p + self._size]

    def prod(self, l, r):
        sml, smr = self._e(), self._e()
        l += self._size
        r += self._size
        while l < r:
            if l & 1:
                sml = self._op(sml, self._d[l])
                l += 1
            if r & 1:
                r -= 1
                smr = self._op(self._d[r], smr)
            l >>= 1
            r >>= 1
        return self._op(sml, smr)

    def all_prod(self):
        return self._d[1]

    def max_right(self, l, f):
        if l == self._n: return self._n
        l += self._size
        sm = self._e()
        while True:
            while l % 2 == 0: l >>= 1
            if not f(self._op(sm, self._d[l])):
                while l < self._size:
                    l <<= 1
                    if f(self._op(sm, self._d[l])):
                        sm = self._op(sm, self._d[l])
                        l += 1
                return l - self._size
            sm = self._op(sm, self._d[l])
            l += 1
            if l & -l == l: break
        return self._n

def op(x, y):
    return max(x, y)

def e():
    return -1

def main():
    input = sys.stdin.readline
    n, q = map(int, input().split())
    A = list(map(int, input().split()))
    seg = SegTree(op, e, n, A)
    for _ in range(q):
        t, a, b = map(int, input().split())
        a -= 1
        if t == 1:
            seg.set(a, b)
        elif t == 2:
            print(seg.prod(a, b))
        else:
            f = lambda x: x < b
            print(seg.max_right(a, f) + 1)

if __name__ == "__main__":
    main()
