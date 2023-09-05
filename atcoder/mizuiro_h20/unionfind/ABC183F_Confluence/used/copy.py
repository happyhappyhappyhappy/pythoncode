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