# ライブラリのインポート
import sys
# import heapq,copy
import pprint as pp
from itertools import accumulate
from collections import Counter
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
N,M=MI()
A=LI()
AA=list(accumulate(A))
xdebug(f"Aの累積和 {AA}")
AC=list(accumulate(A))+[0]
for j in range(0,N+1):
    AC[j]=AC[j]%M
xdebug(f"ACの結果 {AC}")
ACC = Counter(AC)
xdebug(f"Counterに治す {ACC}")
ans = 0
for v in ACC.values():
    ans = ans+(v*(v-1))//2
print(ans)
