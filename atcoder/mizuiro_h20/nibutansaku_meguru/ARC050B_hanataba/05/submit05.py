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

R,B=MI()
x,y=MI()

def isOK(arg):
    R_ = R-arg
    B_ = B-arg
    if R_ < 0:
        return False
    if B_ < 0:
        return False
    total = R_//(x-1)+B_//(y-1)
    if total < arg:
        return False
    else:
        return True


def meguru_bisect(ok,ng):
    while 1 < abs(ng-ok):
        mid = (ng+ok)>>1
        if isOK(mid)==True:
            ok = mid
        else:
            ng = mid
#    xdebug(f"OK-> {ok},NG-> {ng}と差が1になったので閾値設定完了")
    return ok
def pow2(p,n):
    res=1
    while 0 < n:
        n_1= n&1
        if n_1 == 1:
            res=res*p
        p = p*p
        n = n >> 1
    return res
ans = meguru_bisect(0,pow2(10,20))
print(ans)
