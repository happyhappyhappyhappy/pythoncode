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
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def IS(): return sys.stdin.readline().strip()
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
    RES=[[]*N for _ in range(0,N)]
    # xdebug(RES)
    for j in range(0,N):
        his_res=TB[j]
        win=0
        for k in range(0,N):
            if his_res[k] == 'o':
                win=win+1
        RES[win].append(j)
    # algorithm
    # xdebug(RES)
    resStrL=[]
    for j in range(N-1,-1,-1):
        for k in range(0,len(RES[j])):
            resStrL.append(str(RES[j][k]+1))
    result=" ".join(resStrL)
    return result

if __name__ == "__main__":
    N = II()
    TB=[]
    for _ in range(0,N):
        s = IS()
        TB.append(s)
    print("{}".format(solver(N,TB)))
