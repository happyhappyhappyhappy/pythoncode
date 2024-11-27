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

def runlength(N,S):
    res=[("1",3),("0",4)]
    res=list()
    j=0
    while j < N:
        k=j
        ch=S[j]
        while k < N and S[k]==ch:
            k=k+1
        cnt=k-j
        res.append((ch,cnt))
        j=k
    return res,len(res)

def tuple2str(tup):
    ch,cnt=tup
    res=ch*cnt
    return res

def solver():
    # algorithm
    N,K=MI()
    S=input().rstrip()
    RL,RL_LEN=runlength(N,S)
    # 位置交換
    onePos=list()
    for j in range(RL_LEN):
        ch,_=RL[j]
        if ch == "1":
            onePos.append(j)
    sw=onePos[K-1]
    T=RL[sw]
    RL[sw]=RL[sw-1]
    RL[sw-1]=T
    res=""
    stlist=list()
    for j in range(RL_LEN):
        tup=RL[j]
        st=tuple2str(tup)
        stlist.append(st)
    res="".join(stlist)
    return res


if __name__ == "__main__":
    print(solver())
