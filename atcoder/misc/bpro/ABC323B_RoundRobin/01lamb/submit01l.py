# ライブラリのインポート
import sys
# import heapq,copy
import pprint as pp
# from collections import deque
# pypy3用
# import pypyjit
# 再帰制御解放
# pypyjit.set_param('max_unroll_recursion=-1')
# sys.setrecursionlimit(10**6)
from logging import getLogger, StreamHandler, DEBUG

# 入力のマクロ
def II(): return int(sys.stdin.readline())
def SI(): return sys.stdin.readline().strip()
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]

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

def solver(N,TB):
    result = 0
    # xdebug(f"N={N}")
    # xdebug(TB)
    ResT=[]
    for j in range(0,N):
        win = 0
        for k in range(0,N):
            if TB[j][k]=='o':
                win=win+1
        ResT.append([win,j+1])
    # xdebug(f"初期結果テーブル->{ResT}")
    ResTS=sorted(ResT,key=lambda x:[-x[0],x[1]])
    # xdebug(f"ソート後->{ResTS}")
    # algorithm
    resStrL=[]
    for t,P in ResTS:
        resStrL.append(str(P))
    # xdebug(f"resStrL={resStrL}")
    result = " ".join(resStrL)
    return result

if __name__ == "__main__":
    N=II()
    TB=[]
    for _ in range(0,N):
        s = SI()
        TB.append(s)
    print("{}".format(solver(N,TB)))
