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

def solver()->list:
    res = [1,2,3]
    N,M=MI()
    V=[]
    for _ in range(N):
        s=input()
        V.append(s)
    zero=[]
    one=[]
    P=[0]*(N+1)
    P[0]=-1
    for j in range(M):
        zero=[]
        one=[]
        for k in range(N):
            if V[k][j]=="0":
                zero.append(k)
            else:
                one.append(k)
        zero_mem=len(zero)
        one_mem=len(one)
        if zero_mem == 0:
            for x in one:
                P[x+1]+=1
        elif one_mem == 0:
            for x in zero:
                P[x+1]+=1
        elif zero_mem < one_mem:
            for x in zero:
                P[x+1]+=1
        else:
            for x in one:
                P[x+1]+=1
    max_point=max(P)
    res=[]
    for j in range(1,N+1):
        if P[j] == max_point:
            res.append(j)
    return res


if __name__ == "__main__":
    res=solver()
    print(*res)
