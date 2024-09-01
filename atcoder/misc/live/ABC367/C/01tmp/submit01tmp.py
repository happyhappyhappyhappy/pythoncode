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

def dfs(N,K,R,A,result):
    xdebug(f"基本入力 : 数={N}, K={K},R={R},A={A}")
    if len(A)==N:
        xdebug(f"A={A}の長さが{N}になったので計算チェックします")
        if sum(A) % K == 0:
            xdebug("適合しましたので追加します")
            result.append(A.copy())
        else:
            xdebug("適合できませんでした")
        return

def solver():
    result = [[1,2,3],[4,5,6]]
    # algorithm
    N,K=MI()
    R=LI()
    xdebug(f"N={N},K={K},R={R}")
    result=[]
    A=[]
    dfs(N,K,R,A,result)
    return result


if __name__ == "__main__":
    result=solver()
    for r in result:
        print(*r)
