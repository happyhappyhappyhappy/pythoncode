# ライブラリのインポート
import sys
import math
# import heapq,copy
import pprint as pp
# from collections import deque
# pypy3用
import pypyjit
# 再帰制御解放
pypyjit.set_param('max_unroll_recursion=-1')
sys.setrecursionlimit(10**6)
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


def gen_primes_upto(n):
    if n==2:
        return
    table=[True]*n
    sqrtn=int(math.ceil(math.sqrt(n)))
    for j in range(2,sqrtn):
        if table[j]==True:
            for k in range(j*j,n,j):
                table[k]=False
    # 関数の第一解答(=return 2)
    yield 2
    for j in range(3,n,2):
        if table[j]==True:
            # 関数の解答 (=return j)
            yield j

def gen_primes_upto_segment(x):
    if x < 11:
        for p in [2,3,5,7]:
            if p < x:
                yield p
        return
    segsize=int(math.ceil(math.sqrt(x)))
    baseprimes = list(gen_primes_upto(segsize))
    for bp in baseprimes:
        yield bp
    for segstart in range(segsize,x,segsize):
        seg = [True]*segsize
        for bp in baseprimes:
            first_multiple =(
segstart if ((segstart % bp)==0)
else segstart+bp-(segstart%bp)
            )
            for q in range(first_multiple,segstart+segstart,bp):
                seg[q%len(seg)]=False
    start = 1 if ((segstart%2)==0) else 0
    for j in range(start,len(seg),2):
        if seg[j]==True:
            if segstart+j >= n:
                break
            yield segstart+j

D = []
N = 100
for x in gen_primes_upto_segment(N):
    D.append(x)
print(D)
