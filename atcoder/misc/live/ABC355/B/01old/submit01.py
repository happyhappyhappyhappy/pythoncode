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
    ans="No"
    N,M=MI()
    A=LI()
    B=LI()
    A.sort()
    B.sort()
    C=A+B
    C.sort()
    Apos=[0]*N
    for j in range(N):
        x=A[j]
        for k in range(N+M):
            if C[k]==x:
                Apos[j]=k
    for j in range(1,N):
        y=Apos[j]-Apos[j-1]
        if y==1:
            ans="Yes"
    if ans=="No":
        Bpos=[0]*M
        for j in range(M):
            x=B[j]
            for k in range(M+N):
                y=C[k]
                if x==y:
                    Bpos[j]=k
                    break
        for j in range(1,M):
            x = Bpos[j]-Bpos[j-1]
            if x==1:
                ans="Yes"
    return ans

if __name__ == "__main__":
    print(solver())
