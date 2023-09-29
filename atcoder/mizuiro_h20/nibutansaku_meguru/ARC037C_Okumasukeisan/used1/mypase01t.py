# ライブラリのインポート
import sys
# import heapq,copy
import pprint as pp
import bisect
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

N,K = MI()
AList = LI()
BList = LI()
AList.sort()
BList.sort()

def is_ok(arg):
    result = False
    all_under=0
    for a_i in AList:
        b_i = arg//a_i
        cnt = bisect.bisect_right(BList,b_i)
        all_under = all_under + cnt
    result = ( K <= all_under)
    return result

def meguru_bisect(ngpos,okpos):
    while(abs(okpos-ngpos)>1):
        mid = (okpos+ngpos)//2
        check = is_ok(mid)
        if check:
            xdebug(f"OKの位置を{okpos}->{mid}に下げます")
            okpos = mid
        else:
            xdebug(f"NGの位置を{ngpos}->{mid}に上げます")
            ngpos = mid
    xdebug(f"最後のOK値 {okpos}を返します")
    return okpos

def pow2(b,p):
    result = 1
    while 0 < p:
        podd = p & 1
        if podd:
            result=result*b
        b=b*b
        p = (p>>1)
    return result

ok = meguru_bisect(1,pow(10,18)+1)
print(ok)
