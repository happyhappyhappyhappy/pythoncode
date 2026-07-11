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


def solver():
    res = []
    N,M=MI()
    colors=[0]*(N+1)
    D=[[] for _ in range(M+1)]
    kinds=0
    for _ in range(N):
        a,d,b=MI()
        D[d].append((a,b))
        if colors[a]==0:
            kinds+=1
        colors[a]+=1
    for j in range(1,M+1):
        column=D[j]
        for a,b in column:
            if colors[b]==0:
                kinds+=1
            colors[b]+=1
            colors[a]-=1
            if colors[a]==0:
                kinds-=1
        res.append(kinds)
    return res


if __name__ == "__main__":
    res=solver()
    for r in res:
        print(r)
