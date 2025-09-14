# ライブラリのインポート
# import heapq,copy
import pprint as pp
import sys

# from collections import deque
# pypy3用
# import pypyjit
# 再帰制御解放
# pypyjit.set_param('max_unroll_recursion=-1')
# sys.setrecursionlimit(10**6)
from logging import DEBUG, StreamHandler, getLogger

# 入力のマクロ
def II(): return int(sys.stdin.readline())
def SI(): return sys.stdin.readline().strip()
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number:int): return [LI() for _ in range(rows_number)]

# デバッグ出力の作成
logger = getLogger(__name__)
handler = StreamHandler()
handler.setLevel(DEBUG)
logger.setLevel(DEBUG)
logger.addHandler(handler)
logger.propagate = False

# クラス+メソッドを一関数
xdebug=logger.debug
ppp=pp.pprint
# Const
MAXSIZE = ( 1 << 59 ) -1
MINSIZE = -( 1 << 59) + 1

def right90(S):
    Supsidedown=S[::-1]
    Strans=list(zip(*Supsidedown))
    R=[]
    for s in Strans:
        R.append(list(s))
    return R

def difference(N,S,T):
    res=0
    for j in range(N):
        for k in range(N):
            if S[j][k]!=T[j][k]:
                res+=1
    return res

def solver():
    N=II()
    S0=[]
    T=[]
    for _ in range(N):
        s=sys.stdin.readline().strip()
        S0.append(s)
    for _ in range(N):
        s=sys.stdin.readline().strip()
        T.append(s)
    S1=right90(S0)
    S2=right90(S1)
    S3=right90(S2)
    change=[0]*4
    for j in range(4):
        change[j]=j
    change[0]=difference(N,S0,T)
    change[1]=difference(N,S1,T)+1
    change[2]=difference(N,S2,T)+2
    change[3]=difference(N,S3,T)+3
    res = min(change)
    return res

if __name__ == "__main__":
    res=solver()
    print(res)

