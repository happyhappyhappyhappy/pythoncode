from collections import defaultdict

class UnionFind():
    def __init__(self,n):
        self.n=n
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
        res = (x == y)
        if res == True:
            return
        if self.parents[y] < self.parents[x]:
            x,y = y,x
        self.parents[x]=self.parents[x]+self.parents[y]
        self.parents[y]=x
    def size(self,x):
        res = (-1)*self.parents[self.find(x)]
        return res
    def same(self,x,y):
        res = (self.find(x)==self.find(y))
        return res
    def members(self,x):
        root = self.find(x)
        print("[debug]self.n={}".format(self.n))
        lst = [ j for j in range(self.n) if self.find(j) == root]
        return lst
    def roots(self):
        lst = [ j for j,x in enumerate(self.parents) if x < 0]
        return lst
    def group_count(self):
        res = len(self.roots())
        return res
    def all_group_members(self):
        group_members=defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members
    def __str__(self):
        s = '\n'.join(f'{ r } : { m }' for r,m in self.all_group_members().items())
        return s

class UnionFindLabel(UnionFind):
    def __init__(self,labels):
        assert len(labels) == len(set(labels))
        self.n = len(labels)
        self.parents = [-1] * self.n
        self.d =  { x: j for j,x in enumerate(labels)}
        self.d_inv = { j : x for j,x in enumerate(labels)}
    def find_label(self,x):
        return self.d_inv[super().find(self.d[x])]
    def union(self,x,y):
        super().union(self.d[x],self.d[y])
    def size(self,x):
        return super().size(self.d[x])
    def same(self,x,y):
        return super().same(self.d[x],self.d[y])
    def members(self,x):
        root = self.find(self.d[x])
        return [self.d_inv[j] for j in range(self.n) if self.find(j) == root]
    def roots(self):
        return [self.d_inv[j] for j,x in enumerate(self.parents) if x < 0]
    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            print("[debug]self.d_inv[member]={} を追加"
                  .format(self.d_inv[member]))
            group_members[self.d_inv[self.find(member)]].append(self.d_inv[member])
        return group_members

l = ['A','B','C','D','E']
ufl = UnionFindLabel(l)
print(ufl)
ufl.union('A','D')
print(ufl)
ufl.union('D','C')
print(ufl)
ufl.union('E','B')
print(ufl)
print(ufl.find_label('D'))
list2 = [(0,0),(0,1),(1,0),(1,1)]
ufl_t = UnionFindLabel(list2)
print(ufl_t)
ufl_t.union((0,1),(1,0))
print(ufl_t)
ufl_t.union((0,0),(1,0))
print(ufl_t)
