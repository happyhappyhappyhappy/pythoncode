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

def calc(M:str,S:str,T:str):
    lenS=len(S)
    lenT=len(T)
    for j in range(lenT):
        if lenS <= j:
            xdebug(f"高→青 のデータを上回りました。高橋の長さ{len(S)}を返します")
            return len(S)
        if S[j]!=T[j]:
            xdebug(f"互いのデータに齟齬が起こりました {M}{j}番目を返します")
            return j
    xdebug(f"相互の合っている文字は{M}{len(T)}個等しくなってます。ただ、高→青の方が長い可能性があります")
    return len(T)

S,T=SI().split(" ")
xdebug(f"高橋→青木 {S},青木→高橋 {T}")
a=calc("先頭",S,T)
xdebug(f"高橋→青木 {S}と 青木→高橋 {T}は「先頭」 {a}個等しい")
Sr=S[::-1]
Tr=T[::-1]
b=calc("後方",Sr,Tr)
xdebug(f"高橋→青木 {S}と 青木→高橋 {T}は「後方」 {b}個等しい")
if a==len(S) and len(S)==len(T):
    print(f"高橋→青木{S} 青木→高橋{T}は等しい")
elif len(S) <= a+b and len(S)+1==len(T):
    print(f"高橋→青木{S} と青木→高橋{T}は 文字を1文字追加して帰ってきた")
elif len(S) <= a+b+1 and len(S)==len(T)+1:
    print(f"高橋→青木 {S} と青木→高橋 {T}は文字が1文字削られて帰ってきた ")
elif len(S)==a+b+1 and len(S)==len(T):
    print(f"高橋→青木 {S} と青木→高橋 {T}は文字が1文字変換されて帰ってきた ")
else:
    print(f"高橋→青木 {S}と青木→高橋 {T}はデータが根本的に食い違う")
