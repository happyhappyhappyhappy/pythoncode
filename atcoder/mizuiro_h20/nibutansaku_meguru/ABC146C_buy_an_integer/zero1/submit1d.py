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

A,B,X = MI()

def pow2(b,p):
    result=1
    while 0 < p:
        p_and_1=p&1
        if p_and_1 == 1:
            xdebug(f"{b}^{p}を掛けました")
            result=result*b
        b = b*b
        p = p >> 1
    return result

def is_ok(arg1):
    result = False
    xdebug(f"整数 {arg1} は買えるか？")
    nowCheck=A*arg1+B*len(str(arg1))
    xdebug(f"{nowCheck}円です")
    if nowCheck <= X:
        xdebug("OK牧場")
        result = True
    else:
        xdebug("X!!")
        result = False
    return result

def bisect_for_meguru(okarg,ngarg):
    while 1 < (abs(ngarg-okarg)):
        mid = (ngarg+okarg)//2
        if is_ok(mid)==True:
            okarg=mid
        else:
            ngarg=mid
    return okarg

answer=bisect_for_meguru(0,pow2(10,9)+1)
print(answer)
