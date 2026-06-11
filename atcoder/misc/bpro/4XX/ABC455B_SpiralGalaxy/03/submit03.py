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
    H,W=MI()
    G=[]
    for _ in range(H):
        line=input()
        G.append(line)
    for h1 in range(H):
        for h2 in range(h1+1,H+1):
            for w1 in range(W):
                for w2 in range(w1+1,W+1):
                    flag=True
                    for j in range(h1,h2):
                        for k in range(w1,w2):
                            j2=h1+h2-j-1
                            k2=w1+w2-k-1
                            A=G[j][k]
                            B=G[j2][k2]
                            if A!=B:
                                flag=False
                    if flag is True:
                        res+=1

    return res


if __name__ == "__main__":
    res=solver()
    print(res)

