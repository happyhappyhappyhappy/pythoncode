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



def pow2(p,n):
    result = 1
    while 0 < n:
        oddCheck = n&1
        if oddCheck == 1:
            result=result*p
        p=p*p
        n = n >> 1
    return result

def is_ok(t):
    result = False
    cnt = 0
    for j in range(0,len(A)):
        a = A[j]
        cnt = cnt + (a+(t-1))//t
        # cnt = cnt + kiriage(a,t)
    cnt = cnt-N
    # xdebug(f"長さ{t}で切った回数 {cnt} 、これが {K}以下か調べる")
    result = (cnt <= K)
    return result

def m_bisect(ngd,okd):
    while (1 < abs(okd-ngd)):
        mid = (ngd+okd)//2
        check = is_ok(mid)
        if check == True:
            # xdebug(f"OK値とNG値の中間 {mid}はOKだったため OK値{okd}->{mid}に下げます")
            okd = mid
        else:
            # xdebug(f"OK値とNG値の中間 {mid}はNGだったため NG値{ngd}->{mid}に上げます")
            ngd=mid
    # xdebug(f"OK値 {okd} と NG値 {ngd} と境が決まりました")
    return okd


def solver():
    result = 0
    # algorithm
    # xdebug(f"N->{N},K->{K}")
    # xdebug(A)
    MAXDAT = (pow2(10,9))*(2*pow2(10,5))+1
    # MAXDAT = pow2(10,10)+1
    # xdebug(f"最大値{MAXDAT} 固定値でも良いのだが")
    result = m_bisect(0,MAXDAT)
    return result


if __name__ == "__main__":
    global N,K,A
    N,K = MI()
    A = LI()
    A.sort() # Aを整列→書き直す
    print("{}".format(solver()))
