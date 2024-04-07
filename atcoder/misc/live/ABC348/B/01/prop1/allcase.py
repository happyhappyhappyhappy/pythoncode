# ライブラリのインポート
# import heapq,copy
import math
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

def dist(fromP:list,toP:list):
    xdebug(f"{fromP}->{toP}")
    fpx,fpy=fromP
    tpx,tpy=toP
    dis=math.sqrt((fpx-tpx)**2+(fpy-tpy)**2)
    return dis

def solver():
    result = 0
    # algorithm
    N=II()
    G=[]
    for _ in range(N):
        x,y=MI()
        G.append([x,y])
    for j in range(N):
        maxPosi=N
        maxFarNow=0
        for k in range(N-1,-1,-1):
            if j==k:
                xdebug(f"{j=},{k=}と同じ点になるので止めます")
                continue
            else:
                dis=dist(G[j],G[k])
                xdebug(f"{j}->{k} : {dis}")
                if maxFarNow <= dis:
                    maxPosi=k
                    xdebug(f"maxPos最大更新{maxPosi}")
                    maxFarNow=dis
        xdebug(f"{j+1}の時、最大となるのは{maxPosi+1}")
    return result


if __name__ == "__main__":
    print(f"{solver()}")
