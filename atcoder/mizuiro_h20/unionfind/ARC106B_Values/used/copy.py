from collections import defaultdict

class UnionFind():
    def __init__(self,n):
        self.n = n
        self.parents = [-1]*n
    def find(self,x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x]=self.find(self.parents[x])
            return self.parents[x]

    def union(self,x,y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.parents[y] < self.parents[x]:
            x,y = y,x
        self.parents[x] = self.parents[x]+self.parents[y]
        self.parents[y] = x
    def size(self,x):
        res = (-1)*self.parents[self.find(x)]
        return res
    def same(self,x,y):
        ok = (self.find(x)==self.find(y))
        return ok
    def members(self,x):
        root = self.find(x)
        res = [j for j in range(self.n) if self.find(j) == root]
        return res
    def roots(self):
        res = [j for j , x in enumerate(self.parents) if x < 0]
        return res
    def group_count(self):
        return len(self.roots())
    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members
    def __str__(self):
        res = '\n'.join(f'{r} : {m}' for r,m in self.all_group_members().items())
        return res

N,M = MI()
A = list(MI())
B = list(MI())

uf = UnionFind(N)
for j in range(0,M):
# TODO: 2023-08-06 19:37:08 ここから
