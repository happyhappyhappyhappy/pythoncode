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

R,B = MI()
x,y=MI()
wcnt=0

def pow2(p,n):
    result=1
    while 0 < n:
        oddc=n&1
        if oddc == 1:
            result = result*p
        p=p*p
        n=n>>1
    return result

def is_ok(taba):
    Rselect = R-taba
    Bselect = B-taba
    if Rselect <= 0 or Bselect <= 0:
        xdebug(f"検索:{taba}では、そもそも1本ずつ必要という条件は満たせませんNG")
        return False
    cnt = Rselect // (x-1)+Bselect // (y-1)
    result = (taba <= cnt)
    if result == True:
        xdebug(f"検索花束:{taba} 以上の {cnt}が作れるOK")
    else:
        xdebug(f"検索花束:{taba} 以上の {cnt}は作れないNG")
    return result

def m_bisect(ngd,okd):
    global wcnt
    while 1 < abs(ngd-okd):
        wcnt=wcnt+1
        mid = (ngd+okd)//2
        if is_ok(mid):
            xdebug(f"指定していた{mid}は問題ありません OK情報を {okd}->{mid}にします")
            okd = mid
        else:
            xdebug(f"指定していた{mid}は使えません NG情報を {ngd}->{mid}にします")
            ngd = mid
    xdebug(f"okd={okd} と ngd={ngd}の差分が 1になりました")
    return okd

x = m_bisect(pow2(10,18)+1,0)
print(x)
xdebug(f"ループしたのは {wcnt} 回でした")
