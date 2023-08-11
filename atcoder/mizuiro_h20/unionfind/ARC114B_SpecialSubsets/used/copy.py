from collections import defaultdict

class UnionFind():
    def __init__(self,n):
        self.n = n
        self.parents = [-1]*n
    def find(self,x):
        if self.parents[x]<0:
            return x
        xp = self.parents[x]
        self.parents[x]=self.find(xp)
        return self.parents[x]
    def union(self,x,y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.parents[y] < self.parents[x]:
            x,y = y,x
        self.parents[x]=self.parents[x]+self.parents[y]
        self.parents[y]=x

    def size(self,x):
        pm = (self.parents[self.find(x)])*(-1)
        return pm
    def same(self,x,y):
        return self.find(x)==self.find(y)
    def members(self,x):
        root = self.find(x)
        m_l=[j for j in range(0,self.n) if root == self.find(j)]
        return m_l
    def roots(self):
        r_l = [j for j,x in enumerate(self.parents) if x < 0]
    def group_count(self):
        x = self.roots()
        return len(x)
    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(0,self.n):
            group_members[self.find(member)].append(member)
        return group_members
    def __str__(self):
        res_str="\n".join(f"{r}: {m}" for r,m in self.all_group_members().items())
        return res_str
# TODO: ここから 2023-08-11 19:34:12
# TODO データをUnionFindにどうセットするか、どう表示するかを見ておく
