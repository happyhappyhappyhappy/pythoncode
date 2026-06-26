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

def analyse(s):
    if s in {"a","b","c"}:
        return "2"
    if s in {"d","e","f"}:
        return "3"
    if s in {"g","h","i"}:
        return "4"
    if s in {"j","k","l"}:
        return "5"
    if s in {"m","n","o"}:
        return "6"
    if s in {"p","q","r","s"}:
        return "7"
    if s in {"t","u","v"}:
        return "8"
    return "9"

def solver():
    res = ""
    N=II()
    A=input().split(" ")
    G=[]
    for j in range(N):
        s=A[j][0]
        G.append(analyse(s))
    res="".join(G)
    return res


if __name__ == "__main__":
    res=solver()
    print(res)
