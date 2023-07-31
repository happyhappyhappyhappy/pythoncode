from collections import defaultdict
class UnionFind():
    def __init__(self,n):
        self.n = n
        self.parents = [-1]*n
    def find(self,x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]
    def union(self,x,y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.parents[x] > self.parents[y]:
            x,y = y,x
        self.parents[x] = self.parents[x]+self.parents[y]
        self.parents[y] = x
    def size(self,x):
        return -self.parents[self.find(x)]
    def same(self,x,y):
        return self.find(x)==self.find(y)
    def members(self,x):
        root = self.find(x)
        return [j for j in range(self.n) if self.find(j) == root]
    def roots(self):
        ans = [j for j,x in enumerate(self.parents) if x < 0]
        return ans
    def group_count(self):
        return len(self.roots())
    def all_group_members(self):
        group_members = defaunltdist(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

def __str__(self):
    return '\n'.join(f'{r}: {m}' for r,m
                     in self.all_group_members().items())
N,M = map(int,input().split())
uf = UnionFind(N)
for j in range(0,M):
    x,y=map(int,input().split())
    uf.union(x-1,y-1)
ans = 0
for j in range(0,N):
    ans = max(ans,uf.size(j))

print(ans)
