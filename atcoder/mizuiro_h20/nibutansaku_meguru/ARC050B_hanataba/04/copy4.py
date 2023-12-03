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

def isOK(banq):
    R_=R-banq
    B_=B-banq
    if R_ < 0 or B_ < 0:
        return False
    RedBanq=R_//(x-1)
    BlueBanq=B_//(y-1)
    if banq <= (RedBanq+BlueBanq) :
        return True
    else:
        return False

def bisect_meguru(ok,ng):
    while 1 < abs(ng-ok):
        mid = (ng+ok)>>1
        if isOK(mid):
#            xdebug(f"{mid}はOKだったのでこれをokの値にする ng={ng},ok={mid}")
            ok = mid
        else:
#            xdebug(f"{mid}はNGだったのでこれをngの値にする ng={mid},ok={ok}")
            ng=mid
#    xdebug(f"NG={ng},OK={ok}の差が1になったので終了")
    return ok

if __name__ == "__main__":
    print("{}".format(bisect_meguru(0,10**20)))
