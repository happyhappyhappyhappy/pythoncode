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


def check(T:str,S:str):
    xdebug(f"高橋->{T},青木->{S}の場合")
    t=len(T)
    a=len(S)
    minlen=min(t,a)
    endFlug=True
    endPos=0
    for j in range(minlen):
        if T[j]!=S[j]:
            endFlug=False
            endPos=j
            break
    if endFlug is True:
        endPos=minlen
    return endPos

T ="babc"
S ="ababc"
A=check(T,S)
xdebug(f"先頭から同じ文字数は {A=}個です")
Tr=T[::-1]
Sr=S[::-1]
B=check(Tr,Sr)
xdebug(f"逆から同じ文字数は {B=}個です")
result=False
if A==len(T):
    if len(T)==len(S):
        result=True
elif A+B >= len()
