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
def SI(): return sys.stdin.readline().strip()
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




def solver(S):
    result = 0
    # xdebug(S)
    # algorithm
    chrList=[0]*26
    for j in range(0,len(S)):
        nowChr=ord(S[j])-ord('a')
        chrList[nowChr]=chrList[nowChr]+1
    resList=[]
    for j in range(0,26):
        resList.append([chr(j+ord('a')),chrList[j]])
    resSL=sorted(resList,key=lambda x:[-x[1],x[0]])
    result=resSL[0][0]
    return result


if __name__ == "__main__":
    S=SI()
    print("{}".format(solver(S)))
