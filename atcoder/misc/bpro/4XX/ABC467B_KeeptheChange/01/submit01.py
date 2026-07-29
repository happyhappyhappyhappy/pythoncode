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
    res = 0
    N=II()
    D=[]
    for _ in range(N):
        ast,bs,s=input().split(" ")
        a=int(ast)
        b=int(bs)
        f=False
        if s == "take":
            f=True
        D.append((a,b,f))
    Xt=10000
    Xtk=10000
    for a,b,f in D:
        if f is True:
            Xtk-=a
        else:
            Xtk-=b
        Xt-=a
    res=Xt-Xtk
    return res


if __name__ == "__main__":
    res=solver()
    print(res)
