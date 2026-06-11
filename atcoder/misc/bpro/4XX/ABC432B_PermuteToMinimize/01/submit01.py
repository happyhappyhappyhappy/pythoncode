# ライブラリのインポート
# import heapq,copy
import pprint as pp
import sys
from itertools import permutations as perm
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

def list2num(x):
    res=0
    for j in range(len(x)):
        res=res*10+int(x[j])
    return res

def solver():
    res = MAXSIZE
    X=II()
    S=str(X)
    XList=list(perm(S,len(S)))
    for x_each in XList:
        if x_each[0] != "0":
            num = list2num(x_each)
            res=min(res,num)
    return res


if __name__ == "__main__":
    res=solver()
    print(res)
