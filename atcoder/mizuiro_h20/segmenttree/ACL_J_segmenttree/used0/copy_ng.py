# ライブラリのインポート
# 一旦ペンディング
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

class SegTree:
    def __init__(self,op,e,n,v=None):
        self._n=n
        self._op=op
        self._e=e
        self._log=(n-1).bit_length()
        self._size= 1<< self._log
        self._d=[self._e()] * (self._size << 1)
        if v is not None:
            for i in range(self._n):
                self._d[self._size+i]=v[i]
            for i in range(self._size-1,0,-1):
                self._d[i]=self._op(self._d[i<<1],self._d[i<<1 | 1])
    def set(self,p,x):
        p+=self._size
        self._d[p]=x
        while p:
            self._d[p>>1] = self._op(self._d[p],self._d[p^1])
 #           xdebug(f"p>>1 = {p>>1}, p= {p}->{bin(p)} , p^1 = {p^1}->{bin(p^1)}")
            p >>= 1
#        xdebug(f"set後のデータ:{self.__datadump()}")
    def get(self,p):
        return self._d[p+self._size]
    def prod(self,l,r):
        sml,smr = self._e(),self._e()
        l += self._size
        r +=  self._size
        while l < r:
            if l & 1:
                sml = self._op(sml,self._d[l])
                l += 1
            if r & 1:
                r-=1
                smr = self._op(self._d[r],smr)
            l >>= 1
            r >>= 1
        return self._op(sml,smr)
    def all_prod(self):
        return self._d[1]
    def max_right(self,l,f):
        if l == self._n : return self._n
        l += self._size
        sm = self._e()
        while True:
            while l % 2 ==0: l >>= 1
            if not f(self._op(sm,self._d[l])):
                while l < self._size:
                    l <<= 1
                    if f(self._op(sm,self._d[l])):
                        sm = self._op(sm,self._d[l])
                        l += 1
                return l - self._size
            sm = self._op(sm,self._d[l])
            l += 1
#            xdebug(f"all_l={all_l}->{bin(all_l)},l={l}->{bin(l)},(-l)={-l}->{bin(-l)}")
            if l & (-l) == l:break
        return self._n
    # def __datadump(self):
    #     leng  = len(self._d)
    #     res = str([ self._d[j] for j in range(1,leng)])
    #     return res
    # def __str__(self):
    #     res = str([self.get(j) for j in range(self._n)])
    #     return res
def op(x,y):
    return max(x,y)
def e():
    return -1

def main():
    N,Q = MI()
    A = LI()
    G = SegTree(op,e,N,A)
    for _ in range(0,Q):
        t,a,b = MI()
        a -= 1
        if t == 1:
            G.set(a,b)
        elif t==2:
            x = G.prod(a,b)
            print(G.prod(a,b))
        else:
            f = lambda x: x<b
            y = G.max_right(a,f)+1
            print(y)

if __name__ == "__main__":
    main()
