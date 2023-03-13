# ライブラリのインポート
import sys
# from collections import defaultdict
# import heapq,copy
import pprint as pp
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

def solver(G):
    result = "NO"
    for h in range(0,10):
        for w in range(0,10):
            if G[h][w] == 'x':
                G[h][w] = 'v' # 探索済みを入れてしまう

                break

    # algorithm
    return result


if __name__ == "__main__":
    G=[list(input()) for _ in range(10)]
    # print(G)
    print("{}".format(solver(G)))
