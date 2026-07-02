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

def rotate(G):
    Gans=[]
    G180=G[::-1]
    GZ=zip(*G180)
    for r in GZ:
        column="".join(r)
        Gans.append(column)
    return Gans

def solver():
    G = []
    H,_=MI()
    for _ in range(H):
        column=input()
        G.append(column)
    for _ in range(4):
        while "#" not in G[0]:
            G=G[1:]
        G=rotate(G)
    return G


if __name__ == "__main__":
    res=solver()
    for r in res:
        print(r)
