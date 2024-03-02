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

def pow2(p:int,n:int):
    ans=1
    while 0 < n:
        and1 = n & 1
        if and1 == 1:
            ans=ans*p
        p = p * p
        n = n >> 1
    return ans
def palin(p:int):
    pstr=str(p)
    pstrRev = pstr[::-1]
    leng=len(pstr)
    flug = True
    for j in range(leng):
        if pstr[j] != pstrRev[j]:
            flug=False
            break
    if flug is True:
        return True
    else:
        return False
MAXLIMIT=pow2(10,18)
rippou = 1
base=1
rippouList=[]
while rippou < MAXLIMIT:
    rippou = pow2(base,3)
    if palin(rippou) is True:
        rippouList.append(rippou)
    base=base+1
rippouLen=len(rippouList)
N = II()
ans=1
for j in range(rippouLen):
    if  rippouList[j] <= N:
        ans=rippouList[j]
    else:
        break
print(ans)
