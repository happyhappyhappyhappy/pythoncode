# ライブラリのインポート
# import heapq,copy
import pprint as pp
import sys

from collections import defaultdict
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

# S="commencement"
# key=2->value=2
# key=1->value=2
# key=3->value=2
# S="banana"
# key=1->value=1
# key=3->value=1
# key=2->value=1
S="ab"

cb=defaultdict(int)
d=defaultdict(int)
for j in range(len(S)):
    cb[S[j]]=cb[S[j]]+1

for key,value in cb.items():
    xdebug(f"{key=}->{value=}")
    d[value]=d[value]+1

for key,value in d.items():
    xdebug(f"{key=}->{value=}")
