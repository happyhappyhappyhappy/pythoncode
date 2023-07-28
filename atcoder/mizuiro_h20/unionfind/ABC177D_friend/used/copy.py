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
    def all_group_members(self): # TODO: ここから2023-07-28 19:29:08
