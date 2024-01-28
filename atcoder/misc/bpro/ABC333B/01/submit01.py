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


def pat(j):
    if j == 0:
        return 0
    elif j==1:
        return 1
    elif j==2:
        return 2
    elif j==3:
        return 2
    else:
        return 1

def solver(F,W):
    result = "No"
#    xdebug(f"最初:{F},次:{W}")
    S1=ord(F[0])-ord('A')
    S2=ord(F[1])-ord('A')
    T1=ord(W[0])-ord('A')
    T2=ord(W[1])-ord('A')
#    xdebug(f"S:{S1}->{S2},T:{T1}->{T2}")
    # algorithm
    SL=abs(S1-S2)
    TL=abs(T1-T2)
    if pat(SL)==pat(TL):
        result="Yes"
    else:
        result="No"
    return result


if __name__ == "__main__":
    ONET=sys.stdin.readline().rsplit()
    ONE=ONET[0]
    TWOT=sys.stdin.readline().rsplit()
    TWO=TWOT[0]
    print("{}".format(solver(ONE,TWO)))
