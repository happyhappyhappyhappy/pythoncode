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
    res = []
    _,_=MI()
    A=LI()
    B=LI()
    dic={}
    for x in A:
        if x in dic:
            dic[x]+=1
        else:
            dic[x]=1
    for x in B:
        if x in dic:
            dic[x]-=1
    res=[]
    for k,v in dic.copy().items():
        if v <= 0:
            del dic[k]
        else:
            for _ in range(v):
                res.extend(str(k))
    res.sort()
    return res


if __name__ == "__main__":
    res=solver()
    print(*res)
