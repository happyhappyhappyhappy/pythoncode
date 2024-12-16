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
    N=II()
    A=LI()
    nums=dict()
    for j in range(N):
        Ai=A[j]
        k=2
        while k*k <= Ai:
            while Ai % (k*k)==0:
                Ai = Ai // (k*k)
            k+=1
        if Ai in nums:
            nums[Ai]+=1
        else:
            nums[Ai]=1
    if 0 in nums:
        res=(N*(N-1))//2-((N-nums[0])*(N-nums[0]-1))//2
        del nums[0]
    else:
        res=0
    for v in nums.values():
        res=res+(v*(v-1))//2
    return res


if __name__ == "__main__":
    print(solver())
