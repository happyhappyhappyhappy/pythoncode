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
from collections import Counter
from logging import DEBUG, StreamHandler, getLogger
from typing import List
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

def substringSplit(N,K,S)->List:
    res=[]
    for j in range(N-K+1):
        subS=S[j:j+K]
        res.append(subS)
    return res

def solver():
    res = ["yam","ana","kak"]
    N,K=MI()
    S=input().rstrip()
    sub_list=substringSplit(N,K,S)
    subCounter=Counter(sub_list)
    maxcnt=max(subCounter.values())
    res=[]
    for substr,cnt in subCounter.items():
        if cnt==maxcnt:
            res.append(substr)
    res.sort()
    return maxcnt,res


if __name__ == "__main__":
    k,res=solver()
    print(k)
    print(*res)
