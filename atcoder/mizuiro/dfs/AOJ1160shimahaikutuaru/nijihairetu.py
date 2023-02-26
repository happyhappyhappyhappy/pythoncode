# ライブラリのインポート
import sys
# from collections import defaultdict
# import heapq,copy
import pprint as pp
# from collections import deque
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

while 1:
    W,H = MI()
    if W == 0 and H == 0:
        ppp("処理終了")
        break
    print("--高さ {}  幅 {}---".format(H,W))
    M = [[ 2 for _ in range(0,W+2)] for _ in range(0,H+2)]
    for h in range(0,H+2):
            print(" {}".format(M[h]))
