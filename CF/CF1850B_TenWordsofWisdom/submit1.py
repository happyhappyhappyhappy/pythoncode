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
# xdebug=logger.debug
ppp=pp.pprint
# Const
MAXSIZE = ( 1 << 59 ) -1
MINSIZE = -( 1 << 59) + 1

DList=[]
# First Case
# x = [0,-1]
# DList.append(x)
# xdebug(DList)
tc = II()
# xdebug(f"tc={tc}")
for _ in range(0,tc):
    DList=[]
    DList.append([0,-1])
    p = II()
    for _ in range(0,p):
        x,y = MI()
#        xdebug(f"x={x},y={y}")
        DT1=[x,y]
        DT2=[x,-1]
        if x <= 10:
            DList.append(DT1)
        else:
            DList.append(DT2)
    maxWisdom = -2
    vicIndice = 0
    for j in range(0,p+1):
        x = DList[j]
        if maxWisdom < x[1]:
            maxWisdom = x[1]
            vicIndice = j
    print(vicIndice)
