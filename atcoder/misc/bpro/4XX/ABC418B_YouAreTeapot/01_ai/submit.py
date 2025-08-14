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
    res = 0.0
    S=input()
    t_indices=[i for i,char in enumerate(S) if char == "t"]
    Tind=len(t_indices)
    if Tind < 2:
        return 0.0
    for j in range(Tind):
        for k in range(j+1,Tind):
            pos_j=t_indices[j]
            pos_k=t_indices[k]
            Ssub=S[pos_j:pos_k+1]
            Nsub=len(Ssub)
            cnt=k-j+1
            if 3 <= Nsub:
                flq=(cnt-2)/(Nsub-2)
                res=max(res,flq)
    return res

if __name__ == "__main__":
    res=solver()
    print(res)
