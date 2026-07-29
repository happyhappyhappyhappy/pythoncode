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
N=300000
M=300000

def solver():
    res = 0
    r=[0]*M
    c=[0]*M
    rused=[False]*(N+1)
    cused=[False]*(N+1)
    _,m=MI()
    for j in range(m):
        r[j],c[j]=MI()
    for j in range(m-1,-1,-1):
        if (not rused[r[j]]) and (not cused[c[j]]):
            rr=r[j]
            cr=c[j]
            xdebug(f"{j}:rused[{rr}]={rused[rr]} cused[{cr}]={cused[cr]} -> 1plus")
            res+=1
        rused[r[j]]=True
        cused[c[j]]=True
    return res


if __name__ == "__main__":
    res=solver()
    print(res)
