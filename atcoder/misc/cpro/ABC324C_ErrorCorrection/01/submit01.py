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
    for j in range(len(T)):
        if len(S) <= j:
            return len(S)
        if S[j]!=T[j]:
            return j
    return len(T)
def check(S:str,T:str):
    if 1 < abs(len(S)-len(T)):
        return False
    A=calc(S,T)
    Sr=S[::-1]
    Tr=T[::-1]
    B=calc(Sr,Tr)
    if A == len(S) and len(S)==len(T):
        return True
    if len(S)<=A+B and len(S)+1==len(T): # 送信より受信が一文字多い
        return True
    if len(S)-1<=A+B and len(S)-1==len(T): # 送信より受信が一文字少ない
        return True
    if len(S)-1==A+B and len(S)==len(T): # 一文字置換されて返ってきた
        return True
    return False

Nstr,T=SI().split(" ")
N=int(Nstr)
ansL=[]
count=0
for j in range(N):
    S=SI()
    if check(S,T):
        ansL.append(j+1)
        count=count+1
print(count)
print(" ".join(map(str,ansL)))
