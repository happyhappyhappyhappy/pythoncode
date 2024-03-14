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

def solver(N:int,R:list):
    G=[[0]*100 for _ in range(100)]
    for j in range(N):
        A,B,C,D=R[j]
        # xdebug(f"横 {A=},{B=} 縦 {C=},{D=}")
        for x in range(A,B):
            for y in range(C,D):
                G[y][x]=1
    # ppp(f"{G=}")
    cover=0
    for j in range(100):
        cover=cover+sum(G[j])
    return cover
    # algorithm
    # return result

if __name__ == "__main__":
    N=II()
    Rap=[]
    for _ in range(N):
        t=LI()
        Rap.append(t)
    print(f"{solver(N,Rap)}")
