# 全探索を用いた方法 2023/10/02 試作
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

N,A,B,C = MI()
L=[0 for _ in range(0,8)]
CH = [1 for _ in range(0,8)]
xdebug(L)
for j in range(0,N):
    L[j]=II()
xdebug(L)

for j in range(0,N):
    CH[j]=4
xdebug(CH)
result=MAXSIZE-1

def magic(A_bn,B_bn,C_bn):
    mp=0
    xdebug(f"Aに使う竹{A_bn},Bに使う竹{B_bn},Cに使う竹{C_bn}")
    a_len=len(A_bn)
    b_len=len(B_bn)
    c_len=len(C_bn)
    if a_len == 0 or b_len == 0 or c_len == 0:
        xdebug("この竹からはいくら魔法を使っても作れません")
        return MAXSIZE
    mp=mp+10*(a_len-1)+10*(b_len-1)+10*(c_len-1)
    a_sum=sum(A_bn)
    b_sum=sum(B_bn)
    c_sum=sum(C_bn)
    xdebug(f"この方式だと Aの材料 {a_sum},Bの材料 {b_sum},Cの材料 {c_sum}になりますここから伸び縮み魔法を使います")
    # TODO a_sum->A,b_sum->B,c_sum->Cにする伸び縮み魔法1を消費する
    # TODO 2023-10-03 19:32:24
    return mp

for j0 in range(0,CH[0]):
    for j1 in range(0,CH[1]):
        for j2 in range(0,CH[2]):
            for j3 in range(0,CH[3]):
                for j4 in range(0,CH[4]):
                    for j5 in range(0,CH[5]):
                        for j6 in range(0,CH[6]):
                            for j7 in range(0,CH[7]):
                                CLIST=[0 for _ in range(0,8)]
                                A_b = [] # Aに使う竹
                                B_b = [] # Bに使う竹
                                C_b = [] # Cに使う竹
                                Z_b = [] # 使わない竹
                                CLIST[0]=j0
                                CLIST[1]=j1
                                CLIST[2]=j2
                                CLIST[3]=j3
                                CLIST[4]=j4
                                CLIST[5]=j5
                                CLIST[6]=j6
                                CLIST[7]=j7
                                xdebug(CLIST)
                                # https://docs.python.org/ja/3/tutorial/controlflow.html?highlight=match#tut-match
                                # を使って各リストの中身をA_b,B_b,C_bに分ける
                                # 分けた後その値を総値関数に投げて最小を受け取る
                                for k in range(0,N):
                                    if CLIST[k]==1:
                                        A_b.append(L[k])
                                    elif CLIST[k]==2:
                                        B_b.append(L[k])
                                    elif CLIST[k]==3:
                                        C_b.append(L[k])
                                    else:
                                        Z_b.append(L[k])
                                nowresult=magic(A_b,B_b,C_b)
