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

class LazySegment():
    n=0
    node=[]
    lazy=[]
    e = 0
    def __init__(self,V):
        sv = len(V)
        self.n=1
        while self.n < sv:
            self.n=self.n*2
        self.node=[self.e]*(self.n*2-1)
        self.lazy=[self.e]*(self.n*2-1)
        for j in range(0,sv):
            self.node[(self.n-1)+j]=V[j]
        for j in range(self.n-2,-1,-1):
            self.node[j]=self.node[2*j+1]+self.node[2*j+2]
    def eval(self,k,l,r):
        if self.lazy[k]!=self.e:
            self.node[k]=self.node[k]+self.lazy[k]
            if 1 < (r-l):
                self.lazy[2*k+1]=self.lazy[2*k+1]+(self.lazy[k]//2)
                self.lazy[2*k+2]=self.lazy[2*k+2]+(self.lazy[k]//2)
            self.lazy[k]=self.e
    def add(self,a,b,val,k=0,l=0,r=-1):
        if r < 0:
            r = self.n
        # とりあえず初期評価
        self.eval(k,l,r)
        if r <= a or b <= l:
            # 相反するときもう何もしない
            return
        if a <= l and r <= b:
            # 範囲内に含むとき値を足して評価
            self.lazy[k]=self.lazy[k]+(r-l)*val
            self.eval(k,l,r)
        else:
            # まだ交差するときはまず下段にメソッドを飛ばす
            mid = ( l+r) >> 1
            self.add(a,b,val,k*2+1,l,mid)
            self.add(a,b,val,2*k+2,mid,r)
            # 下段で評価しているはずなのでその値を貰う
            self.node[k]=self.node[2*k+1]+self.node[2*k+2]
    def getSum(self,a,b,k=0,l=0,r=-1):
        if r < 0:
            r = self.n
        if r <= a or b <= l:
            return self.e
        # 使うことを判明したのでまず評価
        self.eval(k,l,r)
        if a <= l and r <= b:
            return self.node[k]
        mid = (l+r)>>1
        vl = self.getSum(a,b,2*k+1,l,mid)
        vr = self.getSum(a,b,2*k+2,mid,r)
        return vl+vr
    def __str__(self):
        ans = ["nodeの値"]
        for j in range(0,2*self.n-1):
            if self.node[j] == self.e:
                ans.append("E")
            else:
                ans.append(self.node[j])
        return str(ans)
    def strl(self):
        ans = ["遅延の値"]
        for j in range(0,self.n*2-1):
            if self.lazy[j]==self.e:
                ans.append("E")
            else:
                ans.append(self.lazy[j])
        return str(ans)

N,Q = MI()
V = [0]*N
G = LazySegment(V)
ans = []
for j in range(0,Q):
    query=tuple(MI())
    if query[0]==0:
        dmy,s,t,val=query
        s = s-1
        t = t-1
        G.add(s,t+1,val)
    else:
        dmy,s,t=query
        s = s-1
        t = t-1
        x = G.getSum(s,t+1)
        ans.append(x)
for line in ans:
    print(line)
