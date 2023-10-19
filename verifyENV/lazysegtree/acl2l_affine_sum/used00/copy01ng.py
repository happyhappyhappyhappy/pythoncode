import sys
input=sys.stdin.readline
class lazy_segtree():
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
        for i in range(self.n):
            self.d[self.size+i]=V[i]
        for i in range(self.size-1,0,-1):
            self.update(i)
    def set(self,p,x):
        assert 0 <= p and p < self.n
        p=p+self.size
        for i in range(self.log,0,-1):
            self.push(p>>i)
        self.d[p]=x
        for i in range(1,self.log+1):
            self.update(p>>i)
    def get(self,p):
        assert 0<=p and p < self.n
        for i in range(self.log,0,-1):
            self.push(p>>i)
        return self.d[p]
    def prod(self,l,r):
        assert 0 <= l and l <= r and r <= self.n
        if l==r:return self.e
        l=l+self.size
        r=r+self.size
        for i in range(self.log,0,-1):
            if(((l>>i)<<i)!=l):
                self.push(l>>i)
            if(((r>>i)<<i)!=r):
                self.push(r>>i)
        sml,smr=self.e,self.e
        while(l<r):
            oddl=l&1
            if oddl == 1:
                sml=self.op(sml,self.d[l])
                l=l+1
            oddr=r&1
            if oddr == 1:
                r=r-1
                smr=self.op(self.d[r],smr)
            l>>=1
            r>>=1
        return self.op(sml,smr)
    def all_prod(self):return self.d[1]
    def apply_point(self,p,f):
        assert 0 <= p and p < self.n
        p=p+self.size
        for i in range(self.log,0,-1):
            self.push(p>>i)
        self.d[p]=self.mapping(f,self.d[p])
        for i in range(1,self.log+1):
            self.update(p>>i)
    def apply(self,l,r,f):
        assert 0 <= l and l<=r and r<= self.n
        if l==r:
            return
        l=l+self.size
        r=r+self.size
        for i in range(self.log,0,-1):
            if(((l>>i)<<i)!=l):
                self.push(l>>i)
            if(((r>>i)<<i)!=r):
                self.push((r-1)>>i)
        l2,r2=l,r
        while(l<r):
            oddl=l&1
            if oddl==1:
                self.all_apply(l,f)
                l=l+1
            oddr=r&1
            if oddr==1:
                r=r-1
                self.all_apply(r,f)
            l>>=1
            r>>=1
        l,r=l2,r2
        for i in range(1,self.log+1):
            if(((l>>i)<<i)!=l):
                self.update(l>>i)
            if(((r>>i)<<i)!=r):
                self.update((r-1)>>i)
    def max_right(self,l,g):
        assert 0<=l and l <= self.n
        assert g(self.e)
        if l==self.n:
            return self.n
        l=l+self.size
        for i in range(self.log,0,-1):
            self.push(l>>i)
        sm=self.e
        while(1):
            while(l%2==0):
                l>>=1
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
            twoPow=l&(-l)
            if twoPow==l:
                break
        return self.n
    def min_left(self,r,g):
        assert (0<=r and r<=self.n)
        assert g(self.e)
        if r==0:
            return 0
        r=r+self.size
        for i in range(self.log,0,-1):
            self.push((r-1)>>i)
        sm=self.e
        while(1):
            r=r-1
            while(1<r and (r%2)==1):
                r>>=1
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
            if twoPow == r:
                break
        return 0
    def update(self,k):
        self.d[k]=self.op(self.d[2*k],self.d[2*k+1])
    def all_apply(self,k,f):
        self.d[k]=self.mapping(f,self.d[k])
        if(k<self.size):
            self.lz[k]=self.composition(f,self.lz[k])
    def push(self,k):
        self.all_apply(2*k,self.lz[k])
        self.all_apply(2*k+1,self.lz[k])
        self.lz[k]=self.identity

N,Q=map(int,input().split())
a=[int(i) for i in input().split()]
ans=[]
mod=998243353
def operate(a,b):
    a0=a>>32
    a1=a%(1<<32)
    b0=b>>32
    b1=b%(1<<32)
    return ((a0+b0)%mod)+a1+b1
def mapping(f,x):
    f0=f>>32
    f1=f%(1<<32)
    x0=x>>32
    x1=x%(1<<32)
    return (((f0*x0)%mod)<<32)+x1
def composition(f,g):
    f0=f>>32
    f1=f%(1<<32)
    g0=g>>32
    g1=g%(1<<32)
    return (((f0*g0)%mod)<<32)+((g1*f0+f1)%mod)

G=lazy_segtree([(i<<32)+1 for i in a],operate,0,mapping,composition,1<<32)
for i in range(Q):
    seq=tuple(map(int,input().split()))
    if seq[0]==0:
        dummy,l,r,b,c=seq
        G.apply(l,r,(b<<32)+c)
    else:
        dummy,l,r=seq
        ans.append(G.prod(l,r)>>32)

for line in ans:
    print(line)
