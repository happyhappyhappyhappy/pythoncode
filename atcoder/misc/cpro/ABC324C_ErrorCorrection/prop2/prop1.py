# ライブラリのインポート
# import heapq,copy
import pprint as pp
import sys

# from collections import deque
# pypy3用
# import pypyjit
# 再帰制御解放
# pypyjit.set_param('max_unroll_recursion=-1')
# sys.setrecursionlimit(10**6)
from logging import DEBUG, StreamHandler, getLogger


# 入力のマクロ
def II(): return int(sys.stdin.readline())
def SI(): return sys.stdin.readline().strip()
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number:int): return [LI() for _ in range(rows_number)]

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

def calc(S:str,T:str):
    s=len(S)
    t=len(T)
    for j in range(t):
        if s<=j:
            return s
        if S[j]!=T[j]:
            return j
    return t

SL=SI().split(" ")
T=SL[0]
T2=SL[1]
xdebug(f"高橋→青木 {T}")
xdebug(f"青木→高橋 {T2}")

A=calc(T,T2)
xdebug(f"先頭からの一致個数 {A}個")
Tr=T[::-1]
T2r=T2[::-1]
B=calc(Tr,T2r)
xdebug(f"後方からの一致個数 {B}個")
