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

# https://atcoder.jp/contests/abc197/submissions/21295839
# そのまま-> mainを用いない物 TODO:続き
# 2023-06-08 19:33:07

N = int(input())
A=list(map(int,input().split()))
ANS = MAXSIZE
nowSize=(1<<(N-1))-1

# for j in range(0,1<<(N-1)):
for j in range(0,nowSize):
    binnum = bin(j)
    xdebug("---{} の場合---".format(binnum))
    OR=A[0] # 値
    ORL=[0]
    XOR=[] # リスト
    XORL=[]
    for k in range(0,N-1): #正確には「N-1」個目の区切りは最後の数字の右になる
        chain_no=j>>k
        if(chain_no & 1):
            # 1->区切りを入れない
            xdebug("NO={} -> 左に A[{}]={}を加えます".format(k,k+1,A[k+1]))
            ORL.append(k+1)
            OR = OR|A[k+1]
        else:
            # 0->区切りを入れる
            xdebug("NO={} -> 区切ります ORにA[{}]={}を入れます".format(k,k+1,A[k+1]))
            XORL.append(ORL)
            XOR.append(OR)
            OR=A[k+1]
            ORL=[k+1]
    XOR.append(OR) # 最後のORをXORの位置処理の為に追加する
    XORL.append(ORL)
    xdebug("XOR={}".format(XOR))
    xdebug("XORL={}".format(XORL))
    calc=XOR[0]
    for k in range(1,len(XOR)):
        calc=calc^XOR[k]
    xdebug("Now solver case = {}".format(calc))
    ANS=min(ANS,calc)
print(ANS)
