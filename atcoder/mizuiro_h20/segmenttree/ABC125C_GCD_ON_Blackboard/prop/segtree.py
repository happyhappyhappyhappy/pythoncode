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
def GCD2(a,b):
    if b == 0:
        return a
    else :
        return GCD2(b,a%b)
class SegmentTree:
    n=0
    node=[]
    def __init__(self,A):
        sz = len(A)
        self.n = 1
        while self.n < sz:
            self.n=self.n*2
        self.node=[0]*(self.n*2-1)
        for j in range(0,sz):
            self.node[(self.n-1)+j]=A[j]
        for j in range(self.n-2,-1,-1):
            self.node[j]=GCD2(self.node[j*2+1],self.node[j*2+2])
    def getGCD(self,a,b,k=0,l=0,r=-1):
        if r < 0:
            r = self.n
        if r <= a or b <= l :
            return 0
        if a <= l and r <= b:
            return self.node[k]
        mid = (l+r)>>1
        vl = self.getGCD(a,b,2*k+1,l,mid)
        vr = self.getGCD(a,b,2*k+2,mid,r)
        print(f"{vl} と {vr}")
        return GCD2(vl,vr)
    def __str__(self):
        ans = []
        for j in range(0,self.n*2-1):
            ans.append(self.node[j])
        return str(ans)
N,Q = MI()
