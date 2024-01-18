# ライブラリのインポート
import sys
# import heapq,copy
import pprint as pp
from itertools import accumulate
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

N,K = MI()
LAMP = LI()
xdebug(LAMP)

for j in range(K):
    TABLE=[0]*(N+1)
    for k in range(0,N):
        xdebug(f"テーブル max(0,{k}-{LAMP[k]})に1を足します")
        xdebug(f"テーブル min(N,{k}+{LAMP[k]}+1)に1を引きます")
    xdebug(f"テーブルの結果->{TABLE}")
    LAMP=list(accumulate(TABLE))
    xdebug(f"{j}回目の終了時点のLAMP")
    xdebug(LAMP)
print(*LAMP[:N])
