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
        if self.parents[x]>self.parents[y]:
            tmp = x
            x = y
            y = tmp
        self.parents[x]=self.parents[x]+self.parents[y]
        self.parents[y]=x
    def size(self,x):
        res = (-1)*self.parents[self.find(x)]
        return res
    def same(self,x,y):
        ok = ( self.find(x) == self.find(y) )
        return ok
    def members(self,x):
        root = self.find(x)
        res = [j for j in range(0,self.n) if self.find(j) == root]
        return res
    def roots(self):
        res = [j for j,x in enumerate(self.parents) if x < 0]
    def group_count(self):
        num = self.roots()
        return len(num)
    def all_group_members(self):
        group_members=defaultdict(list)
        for member in range(0,self.n):
            group_members[self.find(member)].append(members)
        return group_members
    def __str__(self):
        res_str="\n".join(f"{r}:{m}" for r,m in self.all_group_members().items())
        return res_str

N,M,K = map(int,input().split())
F = [0]*N # 友好関係
uf = UnionFind(N)
for j in range(0,M):
    a,b = map(int,input().split())
    uf.union(a-1,b-1)
    F[a-1]=F[a-1]+1
    F[b-1]=F[b-1]+1
B = [0]*N # ブロック関係
for j in range(0,K):
    c,d = map(int,input().split())
    if uf.same(c-1,d-1): # 同一グループに存在する
        B[c-1]=B[c-1]+1
        B[d-1]=B[d-1]+1
for j in range(0,N):
#    ans = uf.size(j)-1-F[j]-B[j]
#    print(ans)
    print(uf.size(j)-1-F[j]-B[j])
