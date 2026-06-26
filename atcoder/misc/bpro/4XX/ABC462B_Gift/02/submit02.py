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
    N=II()
    GiveT=[]
    for _ in range(N):
        A=LI()
        GiveT.append(A)
    # xdebug(GiveT)
    GivenT=[[] for _ in range(N)]
    for j in range(N):
        column=GiveT[j]
        for k in range(1,len(column)):
            toP=column[k]
            # xdebug(f"{toP}は{j+1}からプレゼントをもらいました")
            GivenT[toP-1].append(j+1)
    # xdebug(GivenT)
    for j in range(N):
        column=GivenT[j]
        lenC=len(column)
        column=[lenC,*column]
        res.append(column)
    return res


if __name__ == "__main__":
    res=solver()
    for line in res:
        print(*line)
