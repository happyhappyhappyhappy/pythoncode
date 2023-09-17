# ライブラリのインポート
import sys
# import heapq,copy
import pprint as pp
from collections import Counter
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
TC=II()
for _ in range(0,TC):
    cnt = II()
    garr = LI()
    garr.sort()
    # xdebug(f"貰ったリスト {garr}")
    fnum=garr[0]
    c = Counter(garr)
    # xdebug(f"数カウント {c}")
    fc = c[fnum]
    if fc == cnt :
        print("-1")
    else:
        firstL = " ".join(f"{x}" for x in garr[:fc])
        otherL = " ".join(f"{x}" for x in garr[fc:])
        print(len(garr[:fc]))
        print(len(garr[fc:]))
        print(firstL)
        print(otherL)
