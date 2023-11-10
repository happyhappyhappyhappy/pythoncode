import sys


class Node:
    def __init__(self, l, r, val):
        self.l = l
        self.r = r
        self.val = val
        self.lazy = 0

    def propagate(self):
        if self.lazy != 0:
            left = Node(self.l, (self.l + self.r) // 2, self.val)
            right = Node((self.l + self.r) // 2 + 1, self.r, self.val)

            left.val += self.lazy
            right.val += self.lazy

            left.lazy += self.lazy
            right.lazy += self.lazy

            self.lazy = 0
            self.val = min(left.val, right.val)

    def update(self, l, r, x):
        if l > self.r or r < self.l:
            return

        self.propagate()

        if l <= self.l and r >= self.r:
            self.val += x
            self.lazy += x
            return

        left = Node(self.l, (self.l + self.r) // 2, self.val)
        right = Node((self.l + self.r) // 2 + 1, self.r, self.val)

        left.update(l, r, x)
        right.update(l, r, x)

        self.val = min(left.val, right.val)

    def query(self, l, r):
        if l > self.r or r < self.l:
            return float('inf')

        self.propagate()

        if l <= self.l and r >= self.r:
            return self.val

        left = self.query(l, (self.l + self.r) // 2)
        right = self.query((self.l + self.r) // 2 + 1, r)

        return min(left, right)


def main():
    n = int(input())

    A = list(map(int, input().split()))

    tree = build(0, n - 1, A)

    while True:
        q = sys.stdin.readline().strip()
        if q == '-1 -1\n':
            break

        s, t = map(int, q.split())
        cmd, l, r = sys.stdin.readline().strip().split()

        if cmd == 'add':
            tree.update(l, r, x)
        else:
            print(tree.query(l, r))


def build(l, r, A):
    if l == r:
        return Node(l, r, A[l])

    mid = (l + r) // 2
    left = build(l, mid, A)
    right = build(mid + 1, r, A)

    return Node(l, r, min(left.val, right.val))


if __name__ == '__main__':
    main()
