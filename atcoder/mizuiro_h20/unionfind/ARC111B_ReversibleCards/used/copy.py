from collections import defaultdict
class UnionFind():
    def __init__(self,n):
        self.n=n
        self.parents=[-1]*n
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
        if self.parents[y]<self.parents[x]:
            x,y = y,x
        self.parents[x]=self.parents[x]+self.parents[y]
        self.parents[y]=x
    def size(self,x):
        root = self.find(x)
        res = (-1)*self.parents[root]
        return res
    def same(self,x,y):
        xroot = self.find(x)
        yroot = self.find(y)
        ok = (xroot == yroot)
        return ok
    def members(self,x):
        root = self.find(x)
        res = [ j for j in range(0,self.n) if self.find(j) == root ]
        return res
    def roots(self):
        res = [ x for x,p in enumerate(self.parents) if p < 0]
        return res
    def group_count(self):
        x = self.roots()
        return len(x)
    def all_group_members(self):
        group_members=defaultdict(list)
        for member in range(0,self.n):
            k  = self.find(member)
            group_members[k].append(member)
        return group_members
    def __str__(self):
        res = "\n".join(f"{r} : {m}" for r,m in self.all_group_members().items())
        return res
N = int(input())
MAXCOL=400000
CNT = [0]*MAXCOL
uf = UnionFind(MAXCOL)
for j in range(0,N):
    a,b = map(int,input().split())
    a = a-1
    b = b-1
    uf.union(a,b)
    CNT[a]=CNT[a]+1
    CNT[b]=CNT[b]+1
ans = 0
for group in uf.all_group_members().values():
    cnt  = 0
    for x in group:
        cnt=cnt+CNT[x]
    if cnt==0:
        continue
    leng=len(group)
    if cnt == (leng-1)*2:
        ans = ans + (leng-1)
    else:
        ans = ans + leng
print(ans)
