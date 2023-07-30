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

N,A,B,C = MI()
BanbuList=list()
for _ in range(0,N):
    m = II()
    BanbuList.append(m)

def dfs(n,a,b,c):
    if n ==N :
        minR = min(a,b,c)
        if minR == 0:
            # この場合どう増減魔法を用いても達成は出来ない
            return MAXSIZE
        # 達成する場合の増減魔法の量
        # 最後の10*3は最初の1本目に0->X に付ける際だけ合成魔法は
        # 要らないのでこれを削る
        # TODO:2023-07-30 19:30:09 ここから
        magP = abs(a-A)+abs(b-B)+abs(c-C)-(10*3)
        return magP


print(dfs(0,0,0,0))
