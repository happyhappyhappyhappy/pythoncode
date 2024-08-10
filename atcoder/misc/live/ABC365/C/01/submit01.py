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

def isOK(mid,M,A):
    midSum=0
    for a in A:
        midSum+=min(a,mid)
    if midSum <= M:
        return True
    else:
        return False

def m_bisect(M,A):
    ok=0
    ng=MAXSIZE
    while 1 < abs(ng-ok):
        mid=(ng+ok)//2
        if isOK(mid,M,A):
            ok=mid
        else:
            ng=mid
    return ok

def solver():
    result = "infinite"
    # algorithm
    N,M=MI()
    A=LI()
    sumA=sum(A)
    if sumA <= M:
        return result
    else:
        result=0
    result=m_bisect(M,A)
    return result


if __name__ == "__main__":
    print(solver())
