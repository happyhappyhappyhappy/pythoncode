# ライブラリのインポート
# import heapq,copy
import bisect
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
    N=II()
    H_List=[]
    L_List=[]
    for _ in range(N):
        h,leave=MI()
        H_List.append(h)
        L_List.append(leave)
    max_List=[]
    max_value=0
    for j in range(N-1,-1,-1):
        max_value=max(H_List[j],max_value)
        max_List.append(max_value)
    max_List.reverse()
    # xdebug(max_List)
    _=II()
    Q=LI()
    for q in Q:
        index=bisect.bisect_right(L_List,q)
        res.append(max_List[index])
    return res


if __name__ == "__main__":
    res=solver()
    for r in res:
        print(r)
