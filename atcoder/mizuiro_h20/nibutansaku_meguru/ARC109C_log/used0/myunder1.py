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

N = II()

def pow2(n,p):
    res=1
    while 0 < p:
        oddchk = p & 1
        if oddchk==1:
            res = res*n
        n = n*n
        p = p >>1
    return res

def is_ok(L):
    Lunion=((L+1)*L)//2
    checkOK = (Lunion <= (N+1))
#    xdebug(f"長さ1...{L}を1本ずつ作成可能か->{checkOK}")
    return checkOK

def meguru_bisect(ngd,okd):
    while ( 1 < abs(okd-ngd)):
        mid = (okd+ngd)//2
        if is_ok(mid):
 #           xdebug(f"N+1(={N+1})の木から1...{mid}の木を作ることは可能。もう少し増やしてみる")
            okd = mid
        else :
 #           xdebug(f"N+1(={N+1})の木から1...{mid}の木を作ることは不可能。もう少し減らしてみる")
            ngd = mid
 #   xdebug(f"最終的にはN+1(={N+1})の木から1...最大{okd}の{okd}本を作ることが判定")
    return okd

# xdebug(pow2(N,3))
X = meguru_bisect(pow2(10,18),0)
ans = 0
# xdebug(f"まずN+1={N+1}の木を買う:{ans+1}")
ans = ans+1
# xdebug(f"1...{X}までの{X}本作成")
# xdebug(f"{X+1}から{N}までの{N-X}本購入 {ans+N-X}")
ans = ans+N-X
print(f"{ans}")
