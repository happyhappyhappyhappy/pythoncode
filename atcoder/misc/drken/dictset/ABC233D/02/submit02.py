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
    res = 0
    # algorithm
    N,K=MI()
    A=LI()
    # 累積和
    S=[0]*(N+1)
    # 累積和格納辞書
    nums={}
    for j in range(N):
        S[j+1]=S[j]+A[j]
    # 累積和から定数Kを引いた値が以前の累積和にあるかを調べる
    # あればその数を足す
    # なければパス
    for j in range(N+1):
        X=S[j]-K
        if X in nums:
            res+=nums[X]
        if S[j] in nums:
            nums[S[j]]+=1
        else:
            nums[S[j]]=1
    return res

if __name__ == "__main__":
    print(solver())
