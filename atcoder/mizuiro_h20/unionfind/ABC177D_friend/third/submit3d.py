# ライブラリのインポート
import sys
# import heapq,copy
import pprint as pp
from collections import defaultdict
# pypy3用
# import pypyjit
# 再帰制御解放
# pypyjit.set_param('max_unroll_recursion=-1')
# sys.setrecursionlimit(10**6)
from logging import getLogger, StreamHandler, DEBUG

# 入力のマクロ
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]

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


class UnionFind():
    def __init__(self,n):
            self.n=n
            self.parents=[-1]*n
    def find(self,x):
        if self.parents[x]<0:
            return x
        else:
            self.parents[x]=self.find(self.parents[x])
            return self.parents[x]
    def union(self,x,y):
        xroot = self.find(x)
        yroot = self.find(y)
        ok = (xroot == yroot)
        if ok==True:
            return
        if self.parents[yroot]<self.parents[xroot]:
            roottmp = xroot
            xroot = yroot
            yroot = roottmp
        self.parents[xroot]=self.parents[xroot]+self.parents[yroot]
        self.parents[yroot]=x
# UnionFind実装
# 2023-09-01 19:32:36
# TODO: 次のサイトを参考の上実装
# https://note.nkmk.me/python-union-find/



def solver(N,M,Pairs):
    result = 0
    print(f"N={N},M={M}")
    for j in range(0,M):
        a,b = Pairs[j]
        print(f"a_{j} = {a},b_{j}= {b}")
    # algorithm
    return result


if __name__ == "__main__":
    N,M=MI()
    PList=list()
    for _ in range(0,M):
        a,b=MI()
        a=a-1
        b=b-1
        PList.append([a,b])
    print("{}".format(solver(N,M,PList)))
