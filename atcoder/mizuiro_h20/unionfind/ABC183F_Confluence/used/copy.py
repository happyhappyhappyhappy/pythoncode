from collections import defaultdict

class UnionFind():
    def __init__(self,n):
        self.n=n
        self.parents=[-1]*n
    def find(self,x):
        if self.parents[x]<0:
            return x
        else:
            px = self.parents[x]
            px2 = self.find(px)
            self.parents[x]=px2
            return px2
    def union(self,x,y):
        xroot = self.find(x)
        yroot = self.find(y)
        ok = (xroot == yroot)
        if ok:
            return
        if self.parents[yroot] < self.parents[xroot]:
            tmp = xroot
            xroot = yroot
            yroot = tmp
        self.parents[xroot]=self.parents[xroot]+self.parents[yroot]
        self.parents[yroot]=xroot
    def size(self,x):
        xroot = self.find(x)
        res = (-1)*(self.parents[xroot])
        return res
    def same(self,x,y):
        return self.find(x)==self.find(y)
    def members(self,x):
        root = self.find(x)
        res = [ j for j in range(0,self.n) if self.find(j)==root]
        return res
    def roots(self):
        res = [ j for j,x in enumerate(self.parents) if x < 0]
        return res
    def group_count(self):
        return len(self.roots())
    def all_group_members(self):
        group_members = defaultdict(list)
        for m in range(0,self.n):
            group_members[self.find(m)].append(m)
        return group_members
    def __str__(self):
        res = "\n".join(f"{r} : {m}" for r,m in self.all_group_members().items())
        return res

N,Q = map(int,input().split())
C = list(map(int,input().split()))
print(f"C={C}")
D = []
for j in range(0,N):
    d = defaultdict(int)
    d[C[j]]=1
    D.append(d)
uf = UnionFind(N)
for j in range(0,Q):
    q,a,b = map(int,input().split())
    if q==1:
        print(f"{j}の指令,{a}と{b}を合流させる")
        if not uf.same(a-1,b-1):
            a = uf.find(a-1)
            b = uf.find(b-1)
            if uf.parents[b]<uf.parents[a]:
                print(f"数値入れ替え {a} と {b}")
                a,b = b,a
            print(D)
            print(f"{b}から{a}へ持っていかれる。{b}の中身->{D[b].items()}")
            for k,v in D[b].items():
                print(f"loop->k={k},v={v}")
                print(f"D[{a}][{k}]={D[a][k]}")
                D[a][k]=D[a][k]+v
                print(f"D[{a}][{k}]={D[a][k]}")
            uf.union(a,b)
            print(uf)
    else:
        print(f"{j}の指令,人{a}の束にいるクラス{b}の生徒数")
        print(D)
        print(f"D[{uf.find(a-1)}][{b}]")
        x = D[uf.find(a-1)][b]
        print(x)
