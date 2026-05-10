# ライブラリのインポート
# import heapq,copy
import pprint as pp
import sys

# from collections import deque
# pypy3用
# import pypyjit
# 再帰制御解放
# pypyjit.set_param('max_unroll_recursion=-1')
# sys.setrecursionlimit(10**6)
from logging import DEBUG, StreamHandler, getLogger

# 入力のマクロ
def II(): return int(sys.stdin.readline())
def SI(): return sys.stdin.readline().strip()
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number:int): return [LI() for _ in range(rows_number)]

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

def sgn(x):
    if 1 <= x:
        return 1
    elif x <= -1:
        return -1
    else:
        return 0


def solver():
    res = 0
    N=II()
    L=LI()
    for j in range(N):
        tmp=L[j]
        L[j]=tmp*2
    pattern=1<<N
    for p in range(pattern):
        pos=1
        cnt=0
        for bit in range(N):
            nowPos=pos
            porm=1&(p>>bit)
            if porm == 1:
                nowPos=pos+L[bit]
            else:
                nowPos=pos-L[bit]
            lastCheck=sgn(pos)*sgn(nowPos)
            if lastCheck < 0:
                cnt+=1
            pos=nowPos
        res=max(res,cnt)

    return res


if __name__ == "__main__":
    res=solver()
    print(res)

