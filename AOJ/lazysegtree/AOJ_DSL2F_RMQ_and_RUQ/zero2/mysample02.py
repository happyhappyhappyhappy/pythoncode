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
E = (1<<31)-1
class LazySegment():
    n = 0
    lazy = []
    lazyFlag = []
    node = []
    def __init__(self,V):
        sz = len(V)
        self.n=1
        while self.n < sz:
            self.n=self.n*2
        # 枠が決まったのでその分のリストを作る
        self.node = [E]*(self.n*2-1)
        self.lazy = [E]*(self.n*2-1)
        self.lazyFlag = [False]*(self.n*2-1)
        # V->node
        for j in range(0,sz,1):
            # 最下辺は要素n-1からスタート
            self.node[(self.n-1)+j]=V[j]
        # node他の値
        for j in range(self.n-2,-1,-1):
            self.node[j]=min(self.node[j*2+1],self.node[j*2+2])
    def eval(self,k,l,r):
        # 評価メソッド
        if self.lazyFlag[k]:
            # 遅延フラグが立っていたらまず反映させる
            self.node[k]=self.lazy[k]
            if 1 < r - l:
                # お隣でなければ下に情報を更新
                self.lazy[k*2+1]=self.lazy[k]
                self.lazy[k*2+2]=self.lazy[k]
                # 下に遅延フラグを立てる
                self.lazyFlag[k*2+1]=True
                self.lazyFlag[k*2+2]=True
            # このノードは遅延評価終了
            self.lazyFlag[k]=False
    def update(self,a,b,x,k=0,l=0,r=-1):
        # 区間更新メソッド開始
        # もし初期値であれば最右端のn(self.n)をセット
        if r < 0:
            r = self.n
        self.eval(k,l,r)
        if b <= l or r <= a:
            # aとb,lとrが互いに絡まらないことが確定したら処理終了
            return
        if a <= l and r <= b:
            # 包括しているときは、自身のノードを遅延箇所更新の上、評価
            self.lazy[k]=x
            self.lazyFlag[k]=True
            self.eval(k,l,r)
            return
            # この今セットした遅延情報はeval内で更新して貰う
        else:
            # 混合している場合は、下位のノードに処理を願ってから値を貰う
            self.update(a,b,x,k*2+1,l,(l+r)//2)
            self.update(a,b,x,k*2+2,(l+r)//2,r)
            self.node[k]=min(self.node[2*k+1],self.node[2*k+2])
            return
    def find(self,a,b,k=0,l=0,r=-1):
        # 最小値を見つける
        if r < 0:
            # メインから呼び出したときはまず全体を取る
            r = self.n
        # まず自分を遅延評価
        self.eval(k,l,r)
        if b <= l or r <= a:
            # 範囲外の場合は単位元を返す
            return E
        if a <= l and r <= b:
            # 包括している場合は今のノードを返す
            return self.node[k]
        # 混合している場合は下の二つのノードに最小値発見の処理を行う
        vl = self.find(a,b,2*k+1,l,(l+r)//2)
        vr = self.find(a,b,2*k+2,(l+r)//2,r)
        return min(vl,vr)
    def __str__(self):
        ansL=[]
        for j in range(0,2*self.n-1):
            if self.node[j] == E:
                ansL.append("E")
            else:
                ansL.append(self.node[j])
        return str(ansL)
    def strL(self):
        ansL=[]
        for j in range(0,2*self.n-1):
            if self.lazy[j]==E:
                ansL.append("E")
            else:
                ansL.append(self.lazy[j])
        return str(ansL)


N,Q = MI()
V = [E]*N
G = LazySegment(V)
# xdebug(f"G.node={G}")
# xdebug(f"G.lazy={G.strL()}")
ANSL=[]
for j in range(0,Q):
    query=tuple(MI())
    if query[0]==0:
        dmy,s,t,x=query
        msg=f"{s}から{t+1}(閉区間)まで{x}を入れます"
        # xdebug(msg)
        G.update(s,t+1,x)
        # xdebug(f"G:{G}")
        # xdebug(f"GL:{G.strL()}")
    else:
        dmy,s,t=query
        msg=f"{s}から{t+1}(閉区間)までの最小値をもらいます"
        # xdebug(f"今のG:{G}")
        # xdebug(msg)
        x=G.find(s,t+1)
        ANSL.append(x)
        # xdebug(x)
for line in ANSL:
    print(line)
