# ライブラリのインポート
# import heapq,copy
import pprint as pp
import sys

# from collections import deque
# pypy3用
# import pypyjit
# 再帰制御解放
# pypyjit.set_param('max_unroll_recursion=-1')
# sys.setrecursionlimit(10**6)
from logging import DEBUG, StreamHandler, getLogger


# 入力のマクロ
def II(): return int(sys.stdin.readline())
def SI(): return sys.stdin.readline().strip()
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number:int): return [LI() for _ in range(rows_number)]

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
def eq(A:list,B:list):
    result = True
    leng=len(A)
    for j in range(leng):
        if A[j]!=B[j]:
            result=False
    return result

S = SI()
leng=len(S)
flug=False
selLen=leng-1
while 1 <= selLen:
    xdebug(f"{leng=},{selLen=}")
    for j in range(leng-selLen):
        # print(S[j:j+selLen+1])
        Scut=S[j:j+selLen+1]
        xdebug(f"{Scut=}")
        Scutrev=Scut[::-1]
        xdebug(f"{Scutrev=}")
        if eq(Scut,Scutrev):
            xdebug("This is OK")
    selLen=selLen-1
