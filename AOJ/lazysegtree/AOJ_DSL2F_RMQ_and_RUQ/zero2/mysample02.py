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
                self.lazyFlag[k*2+2]=False
            # このノードは遅延評価終了
            self.lazyFlag[k]=False
    def update(self,a,b,x,k=0,l=0,r=-1):
        # 区間更新メソッド開始
        # もし初期値であれば最右端のn(self.n)をセット
        if r < 0:
            r = self.n
        # TODO: まず自分の遅延状況を評価する

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
xdebug(f"G.node={G}")
xdebug(f"G.lazy={G.strL()}")
ANSL=[]
for j in range(0,Q):
    query=tuple(MI())
    if query[0]==0:
        dmy,s,t,x=query
        ANSL.append(f"{s}から{t+1}(閉区間)まで{x}を入れます")
        # G.update(s,t+1,x)
    else:
        dmy,s,t=query
        ANSL.append(f"{s}から{t+1}(閉区間)までの最小値をもらいます")
        # G.find(s,t+1)
for line in ANSL:
    print(line)
