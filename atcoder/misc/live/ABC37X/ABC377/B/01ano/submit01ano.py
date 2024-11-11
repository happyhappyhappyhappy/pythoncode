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
    result = 0
    # algorithm
    N=8
    Field=[]
    for _ in range(N):
        s=input().rstrip()
        Field.append(s)
    # xdebug(f"Field={Field}")
    rookPlace=list()
    avoidPlace=set()
    for j in range(N):
        ln = Field[j]
        for k in range(N):
            if ln[k] == '#':
                avoidPlace.add((j,k))
                rookPlace.append((j,k))
    # xdebug(f"avoidPlace={avoidPlace}")
    # xdebug(f"rookPlace={rookPlace}")
    for ln,rw in rookPlace:
        for j in range(N):
            avoidPlace.add((ln,j))
        for j in range(N):
            avoidPlace.add((j,rw))
    # xdebug(f"avoidPlace={avoidPlace}")
    result=N*N-len(avoidPlace)
    return result


if __name__ == "__main__":
    print(solver())
