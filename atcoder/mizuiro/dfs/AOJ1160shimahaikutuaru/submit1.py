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
    W , H = MI()
    if W == 0 and H == 0:
        break
    # 壁有りの背景作成
    M = [[2 for _ in range(W)] for _ in range(H)]
    # 地図情報を得る
    MT = list()
    for _ in range(H):
        MT.append(LI())
    # 重ね合わせる
    for h in range(H): # TODO: MTの中身をMに重ね合わせる
