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

def runlength(S):
    # res=[("|",3),("-",4)]
    N=len(S)
    j=0
    res=list()
    while j < N:
        k=j
        ch=S[j]
        while k < N and S[k]==ch:
            k+=1
        cnt=k-j
        res.append((ch,cnt))
        j=k
    return res,len(res)

def solver():
    result = list()
    # algorithm
    S=input().rstrip()
    RL,rllen=runlength(S)
    for j in range(rllen):
        ch,cnt=RL[j]
        if ch == "-":
            result.append(cnt)
    return result


if __name__ == "__main__":
    reslist=solver()
    print(*reslist)
