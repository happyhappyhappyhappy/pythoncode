# ライブラリのインポート
# import heapq,copy
from collections import Counter
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




def solver():
    result = "Yes"
    # algorithm
    S=input().rstrip()
    lenS=len(S)
    if lenS % 2 == 1:
        return "No"
    T=lenS  // 2
    for j in range(T):
        if S[2*j] != S[2*j+1]:
            return "No"
    Dic=dict(Counter(S))
    item=list(Dic.values())
    check=True
    for j in range(len(item)):
        if item[j]!=0 and item[j]!=2:
            return "No"
    return result


if __name__ == "__main__":
    print(solver())
