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
    lenS=len(S)
    lenT=len(T)
    for j in range(lenT):
        if lenS <= j:
            return lenS
        if(S[j]!=T[j]):
            return j
    return lenT
xstr,T=SI().split(" ")
x=int(xstr)
print(x)
SList=[]
aList=[]
for _ in range(x):
    ST=SI()
    SList.append(ST)
for j in range(x):
    S=SList[j]
    xdebug(f"j={j}の場合 T={T},SList[{j}]={SList[j]}")
    a=calc(T,SList[j])
    xdebug(f"a={a}")
    aList.append(a)
xdebug(f"{aList=}")
Trev=T[::-1]
bList=[]
for j in range(x):
    S=SList[j]
    Srev=S[::-1]
    b=calc(Srev,Trev)
    bList.append(b)
ans=[]
for j in range(x):
    TTs=SList[j]
    flug=False
    lenTTs=len(TTs)
    leng=aList[j]+bList[j]
    lenT=len(T)
    if leng==lenTTs and lenTTs == lenT:
        flug=True
    if leng >= lenTTs and lenTTs+1 == lenT:
        flug=True
    if leng >= lenTTs-1 and lenTTs-1==lenT:
        flug=True
    if leng == lenTTs-1 and lenTTs == lenT:
        ans.append(str(j+1))
ansStr=" ".join(ans)
print(ansStr)
