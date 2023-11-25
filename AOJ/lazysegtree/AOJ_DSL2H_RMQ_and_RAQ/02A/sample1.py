# ライブラリのインポート
import sys
# import heapq,copy
import pprint as pp
# from collections import deque
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

class LazySegTree():
    def __init__(self,_n,fx,fa,fm,fp,ex,em):
        x = 1
        while x < _n:
            x=x*2
        self.n=x
        self.node=[ex]*(self.n*2-1)
        self.lazy=[em]*(self.n*2-1)
        self.FX=fx
        self.FA=fa
        self.FM=fm
        self.FP=fp
    def testFX(self,a,b):
        return self.FX(a,b)
    def __str__(self):
        ans=[]
        for j in range(0,self.n*2-1):
            if self.node[j]==ex:
                ans.append("e")
            else:
                ans.append(self.node[j])
        return str(ans)

# fx最終的な処理本体->最小値を返す
def fx(x1,x2):
    return min(x1,x2)
# fa lazy:l があったらnode:nにどういう処理をさせたいか->足す
def fa(n,l):
    return d+l
# fm lazyが溜まっているときにさらにlazyが来たらどうするか->足す
def fm(la1,la2):
    return la1+la2
# fp lazyをnodeに移すときにlazyに対する処理をするか->最小値では弄らない
# m = 1にします
def fp(la,m):
    return la*m
ex = (1>>31)-1
em = (1>>31)-1
N,Q=MI()
G = LazySegTree(N,fx,fa,fm,fp,ex,em)
# print(G)
