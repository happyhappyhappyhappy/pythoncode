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
def LLI(rows_number: int): return [LI() for _ in range(rows_number)]

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

def solver(N:int,A:list,Ex:list):
    result = 0
    for j in range(N-1):
        fm,to=Ex[j]
        nowA=A[j]
        send=(nowA//fm)*to
        A[j+1]=A[j+1]+send
    # algorithm
    result=A[N-1]
    return result

if __name__ == "__main__":
    N = II()
    A = LI()
    Ex = []
    for _ in range(N-1):
        a,b=MI()
        Ex.append([a,b])
    print(f"{solver(N,A,Ex)}")
