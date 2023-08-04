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
# MAXSIZE = ( 1 << 59 ) -1
MAXSIZE = 3234566668 # 100000個目の値を最大値にする
# MINSIZE = -( 1 << 59) + 1
LunNum = []
def dfs(x):
    xdebug(f"{ x } に入りました。終了")
    global LunNum
    if x > 100:
        # 調べ終わったので即終了
        return
    # まずこの値は入れる
    xdebug(f"{ x } をLunNumに入れる。")
    LunNum.append(x)
    unit_point = x % 10
    # まず隣通し同じ値
    dfs(unit_point*10+unit_point)
    # 1の位が0,1,2,3,4,5,6,7,8の時一つ足す
    # 9以下(9が入らなければ良い)
    if unit_point < 9:
        dfs(unit_point*10+unit_point+1)
    # 1の位が1,2,3,4,5,6,7,8,9の9つの時一つ減らす
    # 0より大きい(0が入らなければ良い)
    if 0 < unit_point:
        dfs(unit_point*10+unit_point-1)

# 1から10からdfs発火スタート
for x in range(1,11):
    dfs(x)
# LunNumのソート
LunNum.sort()
# 取った値から答えを返す
N = II()
ans = LunNum[N-1]
print(ans)
