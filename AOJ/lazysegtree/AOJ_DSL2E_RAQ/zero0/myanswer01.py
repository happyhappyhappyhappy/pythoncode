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
# 今回の問題の単位元(共通)
E = 0

class LazySegment():
    n = 1
    sz = 1
    # クラス内で設定
    e = E
    node = []
    lazy = []
    def __init__(self,V):
        self.sz = len(V)
        while self.n < self.sz:
            self.n=self.n*2
        self.node=[self.e]*(self.n*2-1)
        self.lazy=[self.e]*(self.n*2-1)
        for j in range(0,self.sz):
            self.node[(self.n-1)+j]=V[j]
        for j in range(self.n-2,-1,-1):
            self.node[j]=self.node[2*j+1]+self.node[2*j+2]
    def eval(self,k,l,r):

        if self.lazy[k]!=self.e:
            # lazyの中身が単位元でなければ行う
            # 自身の反映
            self.node[k]=self.node[k]+self.lazy[k]
            # 最下段ではなければ 1 < (r - l) 下段のlazyを設定
            # ここでは下の二つの節に等しく、後で反映させたい数値を与える
            if 1 < (r - l):
                self.lazy[2*k+1]=self.lazy[2*k+1]+(self.lazy[k]//2)
                self.lazy[2*k+2]=self.lazy[2*k+2]+(self.lazy[k]//2)
            # 今の節の役目完了
            self.lazy[k]=self.e
    def add(self,a,b,x,k=0,l=0,r=-1):
        if r < 0:
            # していない場合は [0,n) 閉区間に注意
            r = self.n
        # 値が揃ったところで評価1
        self.eval(k,l,r)
        if b <= l or r <= a:
            # お互い交点無いときはもう終わり
            return
        if a <= l and r <= b:
            # 包括していたら
            # 1.lazyに値を入れる
            self.lazy[k]=self.lazy[k]+(r-l)*x
            # 2.評価2回目(包括したケースのみ)
            self.eval(k,l,r)
        else:
            # それ以外
            # 下の節二つを呼び出す
            # 次の呼び出しで下の節2つは評価済みになっている
            # これ以上は評価しない
            self.add(a,b,x,2*k+1,l,(l+r)//2)
            self.add(a,b,x,2*k+2,(l+r)//2,r)
            # その後 新しいnode値を持ってくる
            self.node[k]=self.node[2*k+1]+self.node[2*k+2]
    def oneSum(self,a,b,k=0,l=0,r=-1):
        if r < 0:
            r = self.n
        if r <= a or b <= l:
            return self.e
        xdebug(f"getSumでeval呼び出し({a},{b},{k},{l},{r})")
        self.eval(k,l,r)
        if a <= l and r <= b:
            return self.node[k]
        dmyl = self.oneSum(a,b,2*k+1,l,(l+k)//2)
        dmyr = self.oneSum(a,b,2*k+2,(l+k)//2,r)
        return dmyl+dmyr
    def __str__(self):
        ansL=[]
        for j in range(0,self.n*2-1):
            if self.node[j] != self.e:
                ansL.append(self.node[j])
            else:
                ansL.append("E")
        return str(ansL)
    def strL(self):
        ansL=[]
        for j in range(0,self.n*2-1):
            if self.lazy[j] != self.e:
                ansL.append(self.lazy[j])
            else:
                ansL.append("E")
        return str(ansL)
N,Q = MI()
V = [E]*N
G = LazySegment(V)
# xdebug(f"G:{G}")
ansL=[]
for j in range(0,Q):
    query=tuple(MI())
    if query[0]==0:
        dmy,s,t,x=query
        s = s-1
        t = t-1
        G.add(s,t+1,x)
        # ansL.append(f"G.add({s},{t+1},{x})")
        xdebug(G)
        xdebug(f"G Lazy: {G.strL()}")
    else:
        dmy,j=query
        j=j-1
        x = G.oneSum(j,j+1)
        ansL.append(x)
        # ansL.append(f"G.get({j})")
for line in ansL:
    print(line)
