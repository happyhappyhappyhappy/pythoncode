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
    N,M=MI()
    A=LI()
    B=LI()
    res=10**9
    ans_tmp=0
    A_t=A.copy()
    xdebug(f"A_t[{N-1}]に1加えない場合")
    for j in range(N-1):
        k=N-1-j
        a1=A_t[k]
        a2=A_t[k-1]
        b=B[k-1]
        xdebug(f"A[{k}]={a1}とA[{k-1}]={a2} vs B[{k-1}]={b}")
        if (a1+a2)%M != b:
            xdebug(f"余りが一致しないので A[{k-1}]に1追加")
            A_t[k-1]+=1
            ans_tmp+=1
    xdebug(f"加えた数 {ans_tmp}")
    res=min(res,ans_tmp)
    ans_tmp=0
    xdebug(f"A_t[{N-1}]に1加えた場合")
    A_t=A.copy()
    A_t[N-1]+=1
    ans_tmp+=1
    for j in range(N-1):
        k=N-1-j
        a1=A_t[k]
        a2=A_t[k-1]
        b=B[k-1]
        xdebug(f"A[{k}]={a1}とA[{k-1}]={a2} vs B[{k-1}]={b}")
        if (a1+a2)%M!=b:
            xdebug(f"余りが一致しないので A[{k-1}]に1追加")
            A_t[k-1]+=1
            ans_tmp+=1
    xdebug(f"加えた数 {ans_tmp}")
    res=min(res,ans_tmp)
    return res


if __name__ == "__main__":
    res=solver()
    print(res)
