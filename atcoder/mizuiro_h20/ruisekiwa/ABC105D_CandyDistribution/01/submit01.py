# ライブラリのインポート
import sys
# import heapq,copy
import pprint as pp
from collections import Counter
from itertools import accumulate
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
xdebug=logger.debug
ppp=pp.pprint
# Const
MAXSIZE = ( 1 << 59 ) -1
MINSIZE = -( 1 << 59) + 1
N,M=MI()

def solver(A):
    result = 0
    # 0 は初期値
    ACC=list(accumulate(A))+[0]
    for j in range(0,len(ACC)):
        ACC[j]=ACC[j]%M
    ACC_cnt=Counter(ACC)
    for v in ACC_cnt.values():
        result=result+(v*(v-1))//2
    return result


if __name__ == "__main__":
    A_List=LI()
    print("{}".format(solver(A_List)))
