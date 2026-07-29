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
    n=0
    m=0
    idx=0
    res = 0
    r=[0]*(M+1)
    c=[0]*(M+1)
    rplace=[0]*(N+1)
    cplace=[0]*(N+1)
    n,m=MI()
    for j in range(1,m+1):
        r[j],c[j]=MI()
        a=rplace[r[j]]
        xdebug(f"rplace[{r[j]}]={a}")
        if 0 < rplace[r[j]]:
            idx=rplace[r[j]]
            xdebug(f"{j}:解答が一件減ります 列が理由です({rplace[r[j]]}に置いた石)")
            rplace[r[idx]]=0
            cplace[c[idx]]=0
            res-=1
        b=cplace[c[j]]
        xdebug(f"cplace[{c[j]}]={b}")
        if 0 < cplace[c[j]]:
            idx=cplace[c[j]]
            xdebug(f"{j}:解答が一件減ります 行が理由です({cplace[c[j]]}に置いた石)")
            rplace[r[idx]]=0
            cplace[c[idx]]=0
            res-=1
        rplace[r[j]]=j
        cplace[c[j]]=j
        xdebug(f"{j}:({r[j]},{c[j]})に石が置かれました")
        res+=1
    return res


if __name__ == "__main__":
    res=solver()
    print(res)


