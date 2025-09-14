import os
import sys
import pprint as pp

from io import StringIO
ppp=pp.pprint


def right90(S):
    res=[]
    Sjouge=S[::-1]
    Stenchi=list(zip(*Sjouge))
    for x in Stenchi:
        res.append(list(x))
    return res


N=int(sys.stdin.readline())
S=[]
T=[]
for _ in range(N):
    s=input()
    S.append(s)
for _ in range(N):
    s=input()
    T.append(s)
ppp(S)
ppp(right90(S))
ppp(T)
