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


def solver():
    res = MAXSIZE
    N,M=MI()
    A=LI()
    B=LI()
    A1=A.copy()
    A2=A.copy()
    firstCnt=0
    secondCnt=0
    # Aの最後に何も加えない場合
    for j in range(N-1,0,-1):
        if (A1[j]+A1[j-1])%M != B[j-1]:
            A1[j-1]+=1
            firstCnt+=1
    res=min(res,firstCnt)
    # Aの最後に1加える場合
    A2[N-1]+=1
    secondCnt+=1
    for j in range(N-1,0,-1):
        if (A2[j]+A2[j-1])%M != B[j-1]:
            A2[j-1]+=1
            secondCnt+=1
    res=min(res,secondCnt)
    return res


if __name__ == "__main__":
    res=solver()
    print(res)
