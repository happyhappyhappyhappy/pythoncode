# ライブラリのインポート
import sys
# import heapq,copy
import pprint as pp
# from collections import deque
# pypy3用
import pypyjit
# 再帰制御解放
pypyjit.set_param('max_unroll_recursion=-1')
sys.setrecursionlimit(10**6)
from logging import getLogger, StreamHandler, DEBUG

# 入力のマクロ
def II(): return int(sys.stdin.readline())
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

N,A,B,C=MI()
L = [int(input()) for _ in range(0,N)]

xdebug("N=竹 {} 本,A=長さ {},B=長さ {},C=長さ {}".format(N,A,B,C))
xdebug("{}".format(L))
INF = MAXSIZE

def dfs(pos,a,b,c):
    xdebug("選択 {} 本目 a = {} b = {} c = {}に入りました".format(pos,a,b,c))
    if pos == N:
        x = abs(a-A)+abs(b-B)+abs(c-C)-10
        minL = min(a,b,c)
        xdebug("作成した物で最小な長さは {}".format(minL))
        if minL > 0:
            xdebug("最小魔法ポイント {} を返す".format(x))
            return x
        else:
            xdebug("どこかに0のデータがありそうなのでMAXで返却")
            return INF
    # TODO:2023-07-07 19:30:52
    # 4通りの選択検索を行う
    retMin=min(0,0,0,0)
    xdebug("この値を返します {}".format(retMin))
    return retMin
print(dfs(0,0,0,0))
