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
    N=8
    Field=[]
    for _ in range(N):
        ln = input().rstrip()
        Field.append(ln)
    Line=[1]*N
    Row=[1]*N
    for j in range(N):
        ln=Field[j]
        if "#" in ln:
            Line[j]=0
    for j in range(N):
        ln=Field[j]
        for k in range(N):
            if ln[k] == "#":
                Row[k]=0

    result = 0
    # algorithm
    for j in range(N):
        for k in range(N):
            if Line[j]==1 and Row[k]==1:
                result+=1
    return result


if __name__ == "__main__":
    print(solver())
