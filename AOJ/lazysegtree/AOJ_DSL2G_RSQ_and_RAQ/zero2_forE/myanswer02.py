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

INF = (1<<31)-1

class LazySegment():
    sz = 1
    n = 1
    e = 0
    node = []
    lazy = []
    def __init__(self,V):
        self.sz = len(V)
        while self.n < self.sz:
            self.n = self.n*2
        self.node = [self.e]*(2*self.n-1)
        self.lazy = [self.e]*(2*self.n-1)
        for j in range(0,self.sz):
            self.node[(self.n-1)+j]=V[j]
        for j in range(self.n-2,-1,-1):
            self.node[j]=self.node[2*j+1]+self.node[2*j+2]
    def eval(self,k,l,r):
        if self.lazy[k] != 0:
            self.node[k]=self.node[k]+self.lazy[k]
        if 1 < (r - l):
            self.lazy[2*k+1]=self.lazy[2*k+1]+self.lazy[k]//2
            self.lazy[2*k+2]=self.lazy[2*k+2]+self.lazy[k]//2
        self.lazy[k]=self.e
    def add(self,a,b,x,k=0,l=0,r=-1):
        if r < 0:
            r = self.n
        self.eval(k,l,r)
        if b <= l or r <= a:
            return
        if a <= l and r <= b:
            self.lazy[k]=self.lazy[k]+(r-l)*x
            self.eval(k,l,r)
        else:
            self.add(a,b,x,2*k+1,l,(l+r)//2)
            self.add(a,b,x,2*k+2,(l+r)//2,r)
            self.node[k]=self.node[2*k+1]+self.node[2*k+2]
    def getSum(self,a,b,k=0,l=0,r=-1):
        if r < 0:
            r = self.n
        if r <= a or b <= l:
            return self.e
        self.eval(k,l,r)
        if a <= l and r <= b:
            return self.node[k]
        vl = self.getSum(a,b,2*k+1,l,(l+r)//2)
        vr = self.getSum(a,b,2*k+2,(l+r)//2,r)
#        xdebug(f"左から来た値 {vl} 右から来た値 {vr}")
        return vl+vr
    def __str__(self):
        retL=[]
        for j in range(0,self.n*2-1):
            if self.node[j] != self.e:
                retL.append(self.node[j])
            else:
                retL.append("E")
        return str(retL)
    def strL(self):
        retL=[]
        for j in range(0,self.n*2-1):
            if self.lazy[j]!=self.e:
                retL.append(self.lazy[j])
            else:
                retL.append("E")
        return str(retL)

N,Q = MI()
V = [0]*N
G = LazySegment(V)
ANSL = []
for j in range(0,Q):
    query = tuple(MI())
    if query[0]==0:
        dmy,s,t,x=query
        s=s-1
        t=t-1
        G.add(s,t+1,x)
        # ANSL.append(f"要素{s} から 要素{t+1}の閉区間で 値{x} を追加します")
        xdebug(f"G={G}")
    else:
        dmy,s,t=query
        s=s-1
        t=t-1
#        xdebug(f"Query {j} の時の G:{G}")
#        xdebug(f"Query {j} の時の GLazy:{G.strL()}")
        x = G.getSum(s,t+1)
        # ANSL.append(f"要素{s} から 要素{t+1}の閉区間の合計を返します")
        ANSL.append(x)
for line in ANSL:
    print(line)
