import sys
readline = sys.stdin.readline
write = sys.stdout.write
N,Q = map(int,input().split())
INF = 2**31-1
LV = (N-1).bit_length()
N0 = 2**LV
data = [0]*(2*N0)
lazy = [0]*(2*N0)

def gindex(l,r):
    L = l+N0
    R = r+N0
    lm = (L // (L & -L))>>1
    rm = (R // (R & -R))>>1
    while L < R:
        if R <= rm:
            yield R
        if L <= lm:
            yield L
        L >>= 1
        R >>= 1
    while L:
        yield L
        L >>= 1

def propagates(*ids):
    for i in reversed(ids):
        v = lazy[i-1]
        if not v:
            continue
        lazy[2*i-1] += v
        lazy[2*i] += v
        data[2*i-1] += v
        data[2*i] += v
        lazy[i-1] = 0

def update(l,r,x):
    L = N0+l
    R = N0+r
    while L < R:
        oddR = ((R & 1) == 1)
        if oddR:
            R = R-1
            lazy[R-1]=lazy[R-1]+x
            data[R-1]=data[R-1]+x
        oddL = ((L & 1) == 1)
        if oddL:
            lazy[L-1]=lazy[L-1]+x
            data[L-1]=data[L-1]+x
            L = L+1
        L = L // 2
        R = R // 2
    for i in gindex(l,r):
        data[i-1]=min(data[2*i-1],data[2*i])+lazy[i-1]

def query(l,r):
    propagates(*gindex(l,r))
    L = N0+l
    R = N0+r
    s = INF
    while L < R:
        if R & 1:
            R = R-1
            s = min(s,data[R-1])
        if L & 1:
            s = min(s,data[L-1])
            L = L + 1
        L = L//2
        R = R//2
    return s
ans = []
for q in range(Q):
    t,*cmd=map(int,readline().split())
    if t==1:
        s,t=cmd
        val = query(s,t+1)
        ans.append(val)
    else:
        s,t,val=cmd
        update(s,t+1,val)
for line in ans:
    print(line)
