class lazy_segtree():
    def update(self,k):self.d[k]=self.op(self.d[2*k],self.d[2*k+1])
    def all_apply(self,k,f):
        self.d[k]=self.mapping(f,self.d[k])
        if (k<self.size):self.lz[k]=self.composition(f,self.lz[k])
    def push(self,k):
        self.all_apply(2*k,self.lz[k])
        self.all_apply(2*k+1,self.lz[k])
        self.lz[k]=self.identity
    def __init__(self,V,OP,E,MAPPING,COMPOSITION,ID):
        self.n=len(V)
        self.log=(self.n-1).bit_length()
        self.size=1<<self.log
        self.d=[E for i in range(2*self.size)]
        self.lz=[ID for i in range(self.size)]
        self.e=E
        self.op=OP
        self.mapping=MAPPING
        self.composition=COMPOSITION
        self.identity=ID
        for i in range(self.n):self.d[self.size+i]=V[i]
        for i in range(self.size-1,0,-1):self.update(i)
    def set(self,p,x):
        assert 0 <= p and p < self.n
        p+=self.size
        for i in range(self.log,0,-1):self.push(p>>i)
        self.d[p]=x
        for i in range(1,self.log+1):self.update(p>>i)
    def get(self,p):
        assert 0<=p and p < self.n
        p+=self.size
        for i in range(self.log,0,-1):self.push(p>>i)
        return self.d[p]
    def prod(self,l,r):
        assert 0 <= l and l <= r and r <= self.n
        if l==r:return self.e
        l+=self.size
        r+=self.size
        for i in range(self.log,0,-1):
            if (((l>>i)<<i)!=l):self.push(l>>i)
            if (((r>>i)<<i)!=r):self.push(r>>i)
        sml,smr=self.e,self.e
        while(l<r):
            oddl=l&1
            if oddl==1:
                sml=self.op(sml,self.d[l])
                l=l+1
            oddr=r&1
            if oddr==1:
                r=r-1
                smr=self.op(self.d[r],smr)
            l=l>>1
            r=r>>1
        return self.op(sml,smr)
    def all_proud(self):return self.d[1]
    def apply_point(self,p,f):
        assert 0 <= p and p < self.n
        p=p+self.size
        for i in range(self.log,0,-1):self.push(p>>i)
        self.d[p]=self.mapping(f,self.d[p])
        for i in range(1,self.log+1):self.update(p>>i)
    def apply(self,l,r,f):
        assert 0<=l and l<= r and r<=self.n
        if l==r:return
        l=l+self.size
        r=r+self.size
        for i in range(self.log,0,-1):
            if(((l>>i)<<i)!=l):self.push(l>>i)
            if(((r>>i)<<i)!=r):self.push((r-1)>>i)
        l2=l
        r2=r
        while(l<r):
            oddl=l&1
            if oddl==1:
                self.all_apply(l,f)
                l=l+1
            oddr=r&1
            if oddr==1:
                r=r-1
                self.all_apply(r,f)
            l=l>>1
            r=r>>1
        l,r=l2,r2
        for i in range(1,self.log+1):
            if (((l>>i)<<i)!=l):self.update(l>>i)
            if (((r>>i)<<i)!=r):self.update((r-1)>>i)
    def max_right(self,l,g):
        assert 0 <= l and l <= self.n
        assert g(self.e)
        if l==self.n : return self.n
        l=l+self.size
        for j in range(self.log,0,-1):self.push(l>>j)
        sm = self.e
        while(1):
            while(l%2==0):l>>=1
            if not(g(self.op(sm,self.d[l]))):
                while(l<self.size):
                    self.push(l)
                    l=2*l
                    if (g(self.op(sm,self.d[l]))):
                        sm=self.op(sm,self.d[l])
                        l=l+1
                return l-self.size
            sm=self.op(sm,self.d[l])
            l=l+1
            twoPow=l&(-1)
            if twoPow == l:break
        return self.n
    def min_left(self,r,g):
        assert (0 <= r and r<=self.n)
        assert g(self.e)
        if r==0:return 0
        r=r+self.size
        for j in range(self.log,0,-1):
            self.push((r-1)>>j)
        sm=self.e
        while(1):
            r=r-1
            while(1<r and ((r%2)==1)):
                r >>= 1
            if not(g(self.op(self.d[r],sm))):
                while(r<self.size):
                    self.push(r)
                    r=r*2+1
                    if g(self.op(self.d[r],sm)):
                        sm=self.op(self.d[r],sm)
                        r=r-1
                return r+1-self.size
            sm=self.op(self.d[r],sm)
            twoPow=r&(-r)
            if twoPow==r:
                break
        return 0
N,Q = map(int,input().split())
a=[int(i) for i in input().split()]
ans=[]
mod=998244353
def operate(a,b):
    return ((a[0]+b[0])%mod,a[1]+b[1])
def mapping(f,x):
    return ((f[0]*x[0]+x[1]*f[1])%mod,x[1])
def composition(f,g):
    return ((f[0]*g[0])%mod,(g[1]*f[0]+f[1])%mod)

seg=lazy_segtree([(i,1) for i in a],operate,(0,0),mapping,composition,(1,0))
for i in range(Q):
    seq=tuple(map(int,input().split()))
    if seq[0]==0:
        dummy,l,r,b,c=seq
        seg.apply(l,r,(b,c))
    else:
        dummy,l,r=seq
        ans.append(seg.prod(l,r)[0])
for line in ans:
    print(line)
