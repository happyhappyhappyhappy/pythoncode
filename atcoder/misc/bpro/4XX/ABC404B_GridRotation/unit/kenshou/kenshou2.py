import sys
import pprint as pp
ppp=pp.pprint

def right90(S):
    R=[]
    Szip=list(zip(*S))
    for s in Szip:
        sl=list(s)
        R.append(sl[::-1])
    return R

N=int(input())
S=[list(sys.stdin.readline().strip()) for _ in range(N)]
T=[list(sys.stdin.readline().strip()) for _ in range(N)]
ppp(S)
S1=right90(S)
ppp(S1)
ppp(T)


