import sys
import pprint as pp
ppp=pp.pprint
N,M=map(int,sys.stdin.readline().split())
print(f"N={N},M={M}")
G=[]
HF=list("."*(M+2))
G.append(HF)
for _ in range(N):
    x=list("."+(input())+".")
    G.append(x)
G.append(HF)
ppp(G)
