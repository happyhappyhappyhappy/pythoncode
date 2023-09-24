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
# xdebug=logger.debug
ppp=pp.pprint
# Const
MAXSIZE = ( 1 << 59 ) -1
MINSIZE = -( 1 << 59) + 1

A,B,X = MI()
# OKC = 0
def pow2(b,p):
    res = 1
    while 0 < p:
        if (p&1) == 1:
            res = b*res
        b=b*b
        p = p >> 1
    return res

def isOK(arg):
#    global OKC
#    OKC=OKC+1
    res = False
    if A*arg+B*(len(str(arg))) <= X:
       res = True
    return res

def bisect_meg(ng_dat,ok_dat):
    while abs(ng_dat-ok_dat) > 1:
        mid = (ng_dat+ok_dat)//2
 #       xdebug(f"{mid}でどうする？")
        if isOK(mid)==True:
  #          xdebug(f"\tok->Next {mid} ok_dat")
            ok_dat = mid
        else:
   #         xdebug(f"\tok->Next {mid} ng_dat")
            ng_dat = mid
    return ok_dat

answer = bisect_meg(pow2(10,9)+1,0)
print(answer)
# xdebug(f"答えが得られるまでの探索回数 {OKC}")
