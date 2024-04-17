# ライブラリのインポート
# import heapq,copy
import pprint as pp
import sys

from collections import defaultdict
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

def solver():
    S=SI()
    firstD=defaultdict(int)
    lastD=defaultdict(int)
    for j in range(len(S)):
        x=S[j]
        firstD[x]=firstD[x]+1
    for value in firstD.values():
        lastD[value]=lastD[value]+1
    flg=True
    for value in lastD.values():
        if value != 2:
            flg=False
            break
    ans=""
    if flg is True:
        ans="Yes"
    else:
        ans="No"
    return ans


if __name__ == "__main__":
    print(solver())
