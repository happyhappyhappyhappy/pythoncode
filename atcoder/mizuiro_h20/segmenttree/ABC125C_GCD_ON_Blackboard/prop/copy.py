from math import gcd
class segtree():
    n=1
    size=1
    log=2
    d=[0]
    op=None
    e=10**15
    def __init__(self,V,OP,E):
        self.n=len(V)
        self.op=OP
        self.e=E
        self.log=(self.n-1).bit_length()
        self.size=1<<self.log
        self.d=[E for j in range(0,2*self.size)]
        for j in range(self.n):
            self.d[self.size+j]=V[j]
        for j in range(self.size-1,0,-1):
            self.update(j)
    def prod(self,l,r):
        assert 0 <= l and l <= r and r <= self.n
        sml=self.e
        smr=self.e
        l=l+self.size
        r=r+self.size
        while(l<r):
            if(l&1):
                sml=self.op(sml,self.d[l])
                l=l+1
            if(r&1):
                smr=self.op(self.d[r-1],smr)
                r=r-1
            l=l>>1
            r=r>>1
        return self.op(sml,smr)
    def update(self,k):
        self.d[k]=self.op(self.d[2*k],self.d[2*k+1])
    def __str__(self):
        ans = []
        for j in range(0,self.size*2):
            ans.append(self.d[j])
        return str(ans)

V = [2,4,8,3,6]
G=segtree(V,gcd,0)
print(G)
