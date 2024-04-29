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

N=II()
A=LI()
W=[0]*N
for j in range(N):
    A[j]=A[j]-1
    W[A[j]]=j
xdebug(f"A={A}")
xdebug(f"W={W}")
R=[]
for j in range(N-1):
    if A[j]==j:
        continue
    k=W[j]
    xdebug(f"W[{A[j]}]とW[{A[k]}]入れ替え")
    tmp=W[A[j]]
    W[A[j]]=W[A[k]]
    W[A[k]]=tmp
    xdebug(f"W={W}")
    xdebug(f"A[{j}]とA[{k}]入れ替え")
    tmp=A[j]
    A[j]=A[k]
    A[k]=tmp
    xdebug(f"A={A}")
    R.append([j,k])
k=len(R)
print(k)
for j in range(k):
    a,b=R[j]
    a=a+1
    b=b+1
    print(f"{a} {b}")
