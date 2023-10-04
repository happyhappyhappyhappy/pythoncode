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
# xdebug(L)
for j in range(0,N):
    L[j]=II()
# xdebug(L)

for j in range(0,N):
    CH[j]=4
# xdebug(CH)
result=MAXSIZE-1

def magic(A_bn,B_bn,C_bn):
    mp=0
    # xdebug(f"Aに使う竹{A_bn},Bに使う竹{B_bn},Cに使う竹{C_bn}")
    a_len=len(A_bn)
    b_len=len(B_bn)
    c_len=len(C_bn)
    if a_len == 0 or b_len == 0 or c_len == 0:
#        xdebug("この竹からはいくら魔法を使っても作れません")
        return MAXSIZE
    mp=mp+10*(a_len-1)+10*(b_len-1)+10*(c_len-1)
    a_sum=sum(A_bn)
    b_sum=sum(B_bn)
    c_sum=sum(C_bn)
    mp = mp+abs(a_sum-A)+abs(b_sum-B)+abs(c_sum-C)
    # xdebug(f"この竹の組み合わせなら各種魔法併せて{mp}使えば作れます。")
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
                                # xdebug(CLIST)
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
                                if nowresult < result:
                                    # xdebug(f"最小値をChange {result}->{nowresult}")
                                    result = nowresult
print(result)
