from collections import defaultdict
class UnionFind():
    def __init__(self,n):
        self.n=n
        self.parents = [-1]*n
    def find(self,x):
        if self.parents[x]<0:
            return x
        else:
            self.parents[x]=self.find(self.parents[x])
            return self.parents[x]
    def union(self,x,y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.parents[x] > self.parents[y]:
            x,y = y,x
        self.parents[x]=self.parents[x]+self.parents[y]
        self.parents[y]=x
    def size(self,x):
        return (-1)*(self.parents[self.find(x)])
    def same(self,x,y):
        z = self.find(x)==self.find(y)
        if z == True:
            return True
        else:
            return False
    def members(self,x):
        root = self.find(x)
        return [j for j in range(self.n) if self.find(j) == root ]
    def roots(self):
        return [ j for j,x in enumerate(self.parents) if x < 0]
    def group_cound(self):
        return len(self.roots())
    def all_group_members(self):
        group_members=defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members
    def __str__(self):
        return '\n'.join(f'{r} : {m}' for r,m in self.all_group_members().items())

uf = UnionFind(6)
print(uf.parents)
print(uf)
uf.union(0,2)
print(uf.parents)
print(uf)
uf.union(1,3)
print(uf.parents)
print(uf)
uf.union(4,5)
print(uf.parents)
print(uf)
uf.union(1,4)
print(uf.parents)
print(uf)
print(uf.find(0))
print(uf.find(5))
print(uf.size(0))
print(uf.size(4))
print(uf.same(0,2))
