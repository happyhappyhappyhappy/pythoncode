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


def myfloor(a,b):
    d=(a%b+b)%b
    ans=(a-d)//b
    # xdebug(f"{a}を{b}で割ります。割った時の切り捨てを求めます")
    # xdebug(f"手間掛け Ver 誤差 {d},答え {ans}")
    # xdebug(f"そのまんま {a//b}")
    return ans

def solver(Cent,Bet,Left,Right):
    result = 0
    Left=Left-Cent
    Right=Right-Cent
    result = myfloor(Right,Bet)-myfloor(Left-1,Bet)
    # algorithm
    return result


if __name__ == "__main__":
    A,M,L,R=MI()
    print("{}".format(solver(A,M,L,R)))
