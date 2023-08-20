from collections import defaultdict

class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

    def __str__(self):
        return '\n'.join(f'{r}: {m}' for r, m in self.all_group_members().items())


N,M = map(int, input().split())
L = [[0] * 2 for i in range(M)]
for i in range(M):
    L[i][0],L[i][1] = map(int, input().split())

ANS = [0]*M

fuben = N*(N-1)//2
uf = UnionFind(N)
for i in reversed(range(M)):
    ANS[i] = fuben
    if not uf.same(L[i][0]-1,L[i][1]-1):
        fuben -= uf.size(L[i][0]-1)*uf.size(L[i][1]-1)
        uf.union(L[i][0]-1,L[i][1]-1)

for i in range(M):
    print(ANS[i])
