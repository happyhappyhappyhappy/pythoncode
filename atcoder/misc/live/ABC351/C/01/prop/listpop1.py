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

N=II()
F=LI()
T=[]
for j in range(N):
    T.append(F[j])
    while True:
        xdebug(f"ただ今のT={T}")
        if len(T)==1:
            xdebug("Tが1個しかないので終了")
            break
        if T[-1]!=T[-2]:
            xdebug("Tの最後と最後から2番目が異なるので終了")
            break
        if T[-1]==T[-2]:
            k=T[-1]
            T.pop()
            T[-1]=k+1
            xdebug(f"修正後のT={T}")
print(len(T))
