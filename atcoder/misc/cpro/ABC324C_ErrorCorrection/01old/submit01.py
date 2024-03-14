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
#    xdebug(f"送信側 {S},受信側 {T}")
    A=calc(S,T)
    Sr=S[::-1]
    Tr=T[::-1]
    B=calc(Sr,Tr)
    if A==len(S) and len(S)==len(T):
#        xdebug(f"送信 {S} と 受信 {T}は同一")
        return True
    elif len(S)<=A+B and len(S)+1==len(T):
        # 先頭一致+後方一致の個数を送信より上回る→送信に一個追加されたが受信
#        xdebug(f"送信 {S} が 受信 {T}では文字1個追加されて帰ってきた")
        return True
    elif len(S)-1<=A+B and len(S)-1==len(T):
        # 送信から1マイナス が
#        xdebug(f"送信 {S} が 受信 {T}では文字1個削除されて帰ってきた")
        return True
    elif len(S)==A+B+1 and len(S)==len(T):
#        xdebug(f"送信 {S} が 受信 {T}では文字1個置換された")
        return True
#    xdebug(f"送信 {S} と 受信 {T}には関連がない")
    return False

Nstr,T2=SI().split(" ")
N=int(Nstr)
# xdebug(f"候補数{N},青→高へ帰ってきた列{T2}")
S=[""]
ansl=[]
for _ in range(N):
    x=SI()
    S.append(x)

cont=0
for j in range(1,N+1):
    T=S[j]
    if check(T,T2):
#        xdebug(f"ケース{j}")
        cont=cont+1
        ansl.append(str(j))
ans=" ".join(ansl)
print(cont)
print(ans)
