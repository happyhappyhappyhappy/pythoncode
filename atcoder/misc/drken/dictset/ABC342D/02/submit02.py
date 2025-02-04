# Problem: https://atcoder.jp/contests/abc342/tasks/abc342_d
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
    # algorithm
    N=II()
    A=LI()
    num={}
    for j in range(N):
        aj=A[j]
        k=2
        while (k*k) <= aj:
            while aj % (k*k) == 0:
                aj=aj // (k*k)
            k=k+1
        if aj in num:
            num[aj]+=1
        else:
            num[aj]=1
    if 0 in num:
        non_zero=N-num[0]
        res=(N*(N-1))//2-(non_zero*(non_zero-1))//2
        del num[0]
    else:
        res=0
    for v in num.values():
        res=res+(v*(v-1))//2
    return res


if __name__ == "__main__":
    print(solver())
