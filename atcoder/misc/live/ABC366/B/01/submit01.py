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
    # algorithm
    N=II()
    S=[]
    M=0
    for _ in range(N):
        Sstr=input().rsplit()
        S.append(Sstr[0])
        M=max(M,len(Sstr[0]))
    # xdebug(f"S={S}")
    # xdebug(f"M={M}")
    T=[["*"] * N for _ in range(M)]
    for j in range(N):
        Sstr=S[j]
        for k in range(len(Sstr)):
            T[k][N-j-1]=S[j][k]
    for j in range(M):
        while T[j][-1]=="*":
            T[j].pop()
    # xdebug(f"T={T}")
    result=[]
    for j in range(M):
        Tstr="".join(T[j])
        result.append(Tstr)
    return result

if __name__ == "__main__":
    res=solver()
    resstr="\n".join(res)
    print(resstr)
