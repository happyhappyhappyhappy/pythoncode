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
    fpx,fpy=fromP
    tpx,tpy=toP
    dis=math.sqrt((fpx-tpx)**2+(fpy-tpy)**2)
    return dis

def main():
    N=II()
    G=[]
    AnsList=[]
    for _ in range(N):
        x,y=MI()
        G.append([x,y])
    for j in range(N):
        maxPos=N # ダミー
        maxFar=0.0
        for k in range(N-1,-1,-1):
            if k==j:
                # xdebug(f"{k=} と {j=}は同じためジャンプします")
                continue
            else:
                dis=dist(G[j],G[k])
                if maxFar <= dis:
                    # xdebug(f"{j=} から {k=} が大きくなりました")
                    maxPos=k
                    maxFar = dis
        # xdebug(f"{j} においては 最大の位置の最小番号は{maxPos+1}です")
        AnsList.append(maxPos+1)
    ansStr="\n".join(map(str,AnsList))
    return ansStr

if __name__ == "__main__":
    print(main())
