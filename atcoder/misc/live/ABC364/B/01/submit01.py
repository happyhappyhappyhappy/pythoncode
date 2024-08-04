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
    result = [1,1]
    # algorithm
    H,W=MI()
    Si,Sj=MI()
    C=[]
    for _ in range(H):
        Cd=list(input())
        C.append(Cd)
    X=input()
    Si-=1
    Sj-=1
    Xlen=len(X)
    for j in range(Xlen):
        Si_t=Si
        Sj_t=Sj
        if X[j] == "U":
            Si_t-=1
            if 0 <= Si_t:
                if C[Si_t][Sj_t]==".":
                    Si=Si_t
                    Sj=Sj_t
        elif X[j] == "D":
            Si_t+=1
            if Si_t<H:
                if C[Si_t][Sj_t]==".":
                    Si=Si_t
                    Sj=Sj_t
        elif X[j] == "L":
            Sj_t-=1
            if 0<=Sj_t:
                if C[Si_t][Sj_t]==".":
                    Si=Si_t
                    Sj=Sj_t
        elif X[j] == "R":
            Sj_t+=1
            if Sj_t < W:
                if C[Si_t][Sj_t]==".":
                    Si=Si_t
                    Sj=Sj_t
    result=[Si+1,Sj+1]
    return result


if __name__ == "__main__":
    result=solver()
    res_str=" ".join(map(str,result))
    print(res_str)
