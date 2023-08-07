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

N,M = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
print(f"A = {A}")
print(f"B = {B}")

uf = UnionFind(N)
for j in range(0,M):
    c,d = map(int,input().split())
    print(f"c = { c-1 } <=> { d-1 } = d")
    uf.union(c-1,d-1)
    print(f"---- プロセス { j+1 } での結果 ----")
    print(uf)


ans = True
GM = uf.all_group_members()
for v in GM.values():
    print(f" { v } で考える")
    temp = 0
    for j in v:
        temp = temp + (A[j]-B[j])
    if (ans and (temp == 0)):
        ans = True

if ans:
    print("Yes")
else:
    print("No")
