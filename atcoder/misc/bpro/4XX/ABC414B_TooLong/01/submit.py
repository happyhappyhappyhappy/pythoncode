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
    res = ""
    N=II()
    Data=[]
    for _ in range(N):
        s,n=input().split(" ")
        s=str(s)
        n=int(n)
        Data.append([s,n])
    sum_length=0
    for j in range(N):
        n=Data[j][1]
        sum_length+=n
        if 100 < sum_length:
            return "Too Long"
    for j in range(N):
        s=Data[j][0]
        n=Data[j][1]
        res+=s*n
    return res


if __name__ == "__main__":
    res=solver()
    print(res)
