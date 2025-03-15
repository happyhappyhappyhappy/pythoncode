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
    res = [["#","#"],["#","#"]] # Dummy
    # algorithm
    N=II()
    res=[["#"]*N for _ in range(N)]
    for i in range(1,N+1):
        j = N+1-i
        if i <= j:
            if i % 2 == 1:
                for ipaint in range(i,j+1):
                    for jpaint in range(i,j+1):
                        res[ipaint-1][jpaint-1]="#"
                        xdebug(f"({ipaint-1},{jpaint-1})を#で塗ります")
            else:
                for ipaint in range(i,j+1):
                    for jpaint in range(i,j+1):
                        res[ipaint-1][jpaint-1]="."
                        xdebug(f"({ipaint-1},{jpaint-1})を.で塗ります")
    return res


if __name__ == "__main__":
    res=solver()
    reslen=len(res)
    for j in range(reslen):
        one=res[j]
        x="".join(one)
        print(x,flush=True)
