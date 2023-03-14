# ライブラリのインポート
import sys
# from collections import defaultdict
# import heapq,copy
import pprint as pp
import copy
from collections import deque
from logging import getLogger, StreamHandler, DEBUG

# 入力のマクロ
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split('')))
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

def isgo(G,posh,posw):
    # TODO: ここをコーディング
    # posh,posw 両方0未満->X
    # posh,posw 両方10以上->X
    # 海である
    # return false
    return true

def solver(G):
    result = "NO"

    for h in range(0,10):
        for w in range(0,10):
            if G[h][w] == 'x':
                G_c=copy.deepcopy(G)
                G_c[h][w] = 'v' # 探索済みを入れてしまう
                dh = [1,0,-1,0]
                dw = [0,1,0,-1]
                dq = deque([h,w])
                while len(dq) != 0:
                    [posh,posw] = dq.pop()
                    for x in range(0,4):
                        next_h = posh + dh[x]
                        next_w = posw + dw[x]

                break

    # algorithm
    return result


if __name__ == "__main__":
    G=[list(input()) for _ in range(10)]
    # print(G)
    print("{}".format(solver(G)))
