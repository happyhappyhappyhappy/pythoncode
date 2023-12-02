# ライブラリのインポート
import sys
import io
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

_INPUT = """\
6 7
0 1 3 1
0 2 4 -2
1 0 5
1 0 1
0 3 5 3
1 3 4
1 0 5
"""
sys.stdin = io.StringIO(_INPUT)

N,Q = MI()
for j in range(0,Q):
    queue=tuple(MI())
    if queue[0]==0:
        _,s,t,val=queue
        print(f"G.update({s},{t+1})={val}")
    else:
        _,s,t=queue
        print(f"G.getSum({s},{t+1})")
