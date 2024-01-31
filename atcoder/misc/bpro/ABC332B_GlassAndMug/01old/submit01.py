# ライブラリのインポート
import sys
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




def solver(K,G,M):
    result = "result"
    xdebug(f"回数 {K},グラス {G},マグカップ {M}")
    # algorithm
    g=0
    m=0
    for _ in range(0,K):
        if g==G:
            g=0
        elif m==0:
            m=M
        else :
            while g<G and 0<m:
                m=m-1
                g=g+1
    result = " ".join(map(str,[g,m]))
    return result


if __name__ == "__main__":
    K,G,M = MI()
    print("{}".format(solver(K,G,M)))
