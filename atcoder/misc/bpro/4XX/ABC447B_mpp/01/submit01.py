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


def atoi(x):
    return ord(x)-ord("a")

def itoa(x):
    return chr(ord("a")+x)

def solver():
    res = ""
    S=list(input())
    B=[0]*26
    for j in range(len(S)):
        pos=atoi(S[j])
        B[pos]+=1
    maxChr=max(B)
    D=set()
    for j in range(26):
        if B[j] == maxChr:
            maxC=itoa(j)
            D.add(maxC)
    ans=[c for c in S if c not in D]
    res="".join(ans)
    return res


if __name__ == "__main__":
    res=solver()
    print(res)
