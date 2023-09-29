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

X,K=MI()
AList=LI()
BList=LI()
AList.sort()
BList.sort()

def pow2(b,p):
    result = 1
    while (0 < p):
        podd = p & 1
        if podd:
            result=result*b
        p = p>>1
        b = b*b
    return result

def is_ok(MID):
    result = False
    CNT=0
    for ai in AList:
        bi = MID//ai
        now_cnt=bisect_right(BList,bi)
        CNT=CNT+now_cnt
    result = (K<=CNT)
    return result

def meguru_bisect(ngnum,oknum):
    while(abs(oknum-ngnum)>1):
        mid = (oknum+ngnum)//2
        checker = is_ok(mid)
        if checker:
            # xdebug(f"OKの値を {oknum} >= {mid} に下げてみます")
            oknum = mid
        else:
            # xdebug(f"NGの値を {ngnum} <= {mid}と上げてみます")
            ngnum = mid
    return oknum

ans = meguru_bisect(1,pow2(10,18)+1)
print(ans)
