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

def solver(S:str):
    codeCnt=[0]*26
    for j in range(26):
        codeCnt[j]=S.count(chr(j+ord("a")))
    ansCnt=[]
    for j in range(26):
        x = chr(ord("a")+j)
        ansCnt.append([x,codeCnt[j]])
    # algorithm
    # print(ansCnt)
    ansCnt.sort(key=lambda x:[-x[1],x[0]])
    return ansCnt[0][0]

if __name__ == "__main__":
    S=SI()
    print(f"{solver(S)}")
