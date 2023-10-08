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

# 切り上げ関数
# floorを使うと誤差が出やすいのでこの様に求めると良い
# https://bit.ly/3LSLZCd
def kiriage(x,y):
    z = (-1)*((-x)//y)
    return z

def pow2(p,n):
    result = 1
    while 0 < n:
        oddCheck=n & 1
        if oddCheck == 1:
            result=result*p
        p=p*p
        n=n>>1
    return result

def is_ok(t):
    logs=0 # 作った丸太達(ざっくり)
    for a in A:
        # こうすれば長い尺(t)で切ったのも一旦切ると設定できる
        # 最後に差し引く
        logs=logs+kiriage(a,t)
    cnt = logs-N # できた丸太から最初の1本目は取り除いたのが切った回数
    if cnt <= K:
        return True
    else:
        return False

def  m_bisect(ng,ok):
    while (1 < abs(ok-ng)):
        mid = (ok+ng)>>1
        if is_ok(mid):
#            xdebug(f"{mid}はOKの為 {ok}->{mid}と値を小さくしてみます")
            ok=mid
        else:
#            xdebug(f"{mid}はNGの為 {ng}->{mid}と値を大きくしてみます")
            ng=mid
#    xdebug(f"OK={ok},NG={ng}と差が1になりました 終了")
    return ok

def solver():
    result = m_bisect(0,pow2(10,10)+1)
    # algorithm
    return result


if __name__ == "__main__":
    global N,K,A
    N,K=MI()
    A=LI()
    print("{}".format(solver()))
