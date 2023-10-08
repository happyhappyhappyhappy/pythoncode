# ライブラリのインポート
import sys
# import heapq,copy
import pprint as pp
from bisect import bisect_right
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

def pow2(b,n):
    result = 1
    while 0 < n:
        oddcheck=n&1
        if oddcheck==1:
            result = result*b
        b=b*b
        n=n>>1
    return result

def isOK(num):
    result=False
    pos=0
    for ai in A:
        basem=num // ai
        now_pos=bisect_right(B,basem)
        pos=pos+now_pos
    if K <= pos: # ここどうだっけ
        result = True
    # if result:
    #     xdebug(f"整数{num} は {K}番目以上の所におかれるOK")
    # else:
    #     xdebug(f"整数{num} は {K}番目未満の所におかれるNG")
    return result

def m_bisect(ngint,okint):
    while 1 < abs(okint-ngint):
        mid=(okint+ngint)//2
        if isOK(mid)==True:
            # xdebug(f"OKなので位置を{okint}から{mid}に下げる")
            okint = mid
        else:
            # xdebug(f"NGなので位置を{ngint}から{mid}に上げる")
            ngint = mid
    # xdebug(f"NG値 {ngint} <-> OK値 {okint}の差が1になりました")
    return okint

def solver():
    result = 0
    result = m_bisect(1,pow2(10,18)+1)
    # algorithm
    return result

# def answer():
#     xdebug("---逐次解答---")
#     ANSL=[]
#     for aa in A:
#         for bb in B:
#             ANSL.append(aa*bb)
#     ANSL.sort()
#     for x in range(0,len(ANSL)):
#         xdebug(f"左から[{x+1}]番目->{ANSL[x]}")
#         if (K == x+1):
#             xdebug(f"\tこれが答え {K}番目")

if __name__ == "__main__":
    global N,K,A,B
    N,K=MI()
    A=LI()
    A.sort()
    B=LI()
    B.sort()
    print("{}".format(solver()))
#    answer()
