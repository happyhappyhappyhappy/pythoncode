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

N = II()

def dfs(n,has3,has5,has7,L):
    if n > N:
        return
    else:
        if has3 and has5 and has7:
#            xdebug("{} が条件に満たしているので回答リストに入れます".format(n))
            L.append(n)
        dfs(n*10+3,True,has5,has7,L)
        dfs(n*10+5,has3,True,has7,L)
        dfs(n*10+7,has3,has5,True,L)

L = list()
dfs(0,False,False,False,L)
ans = len(L)
print(ans)
