# ライブラリのインポート
import sys
# import heapq,copy
import pprint as pp
from itertools import accumulate
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
MAXTIME=2*pow(10,5)+1

# N: 人数 W: 給湯器が与えられる分単位の給湯量
# s : 各自が需要開始する時間, t : 各自が需要完了する時間 p: 利用量
# tはその時間そのものを含まない。実質利用するのは t-1まで。
# いもす法ではtキッカリにp*(-1)を設定すれば良い。

N,W = MI()
s=[]
t=[]
p=[]
for _ in range(0,N):
    s1,t1,p1=MI()
    s.append(s1)
    t.append(t1)
    p.append(p1)
# b :まず各自の需要量を打ち込む。
b=[0]*(MAXTIME+1)
for j in range(0,N):
    sta = s[j]
    sto = t[j]
    quan = p[j]
    b[sta]=b[sta]+quan
    b[sto]=b[sto]-quan
acc = list(accumulate(b))
# twen=""
# for j in range(0,20):
#     twen=twen+str(acc[j])+"  "
# print(twen)
acc.sort(reverse=True)
watermax=acc[0]
if W < watermax:
    print("No")
else:
    print("Yes")
