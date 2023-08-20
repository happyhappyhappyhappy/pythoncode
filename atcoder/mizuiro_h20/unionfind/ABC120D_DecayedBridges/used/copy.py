from collections import defaultdict

class UnionFind():
    def __init__(self,n):
        self.n=n
        self.parents=[-1 for _ in range(0,n)]
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
        res = (-1)*(self.parents[self.find(x)])
        return res
    def same(self,x,y):
        xroot = self.find(x)
        yroot = self.find(y)
        ok = (xroot == yroot)
        return ok
    def members(self,x):
        root = self.find(x)
        res_list = [j for j in range(0,self.n) if self.find(j) == root]
        return res_list
    def roots(self):
        res_list = [j for j,x in enumerate(self.parents) if x < 0]
        return res_list
    def group_count(self):
        res = len(self.roots())
        return res
    def all_group_members(self):
        group_members=defaultdict(list)
        for m in range(0,self.n):
            group_members[self.find(m)].append(m)
        return group_members
    def __str__(self):
        res_str="\n".join(f"{r} : {m}" for r,m in self.all_group_members.items())
        return res_str

N,M = map(int,input().split())
L = [ [0]*2 for _ in range(0,M) ]
for j in range(0,M):
    L[j][0],L[j][1] =map(int,input().split())

ANS = [0]*M
FB = (N*(N-1))//2
uf = UnionFind(N)
for j in reversed(range(0,M)):
    ANS[j]=FB
    chk = uf.same(L[j][0]-1,L[j][1]-1)
    if chk == False:
        FB=FB-uf.size(L[j][0]-1)*uf.size(L[j][1]-1)
        uf.union(L[j][0]-1,L[j][1]-1)

for j in range(0,M):
    print(ANS[j])
