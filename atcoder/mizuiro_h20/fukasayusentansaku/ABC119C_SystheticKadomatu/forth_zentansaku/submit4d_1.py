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
CH = [0 for _ in range(0,9)]
xdebug(L)
for j in range(0,N):
    L[j]=II()
xdebug(L)

for j in range(0,N):
    CH[j]=4
A_b = [] # Aに使う竹
B_b = [] # Bに使う竹
C_b = [] # Cに使う竹
Z_b = [] # 使わない竹

for j0 in range(0,CH[0]):
    for j1 in range(0,CH[1]):
        for j2 in range(0,CH[2]):
            for j3 in range(0,CH[3]):
                for j4 in range(0,CH[4]):
                    for j5 in range(0,CH[5]):
                        for j6 in range(0,CH[6]):
                            for j7 in range(0,CH[7]):
                                # はまった ペンディング
