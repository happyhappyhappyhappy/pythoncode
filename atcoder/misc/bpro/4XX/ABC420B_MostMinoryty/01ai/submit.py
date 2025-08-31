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


def solver():
    N,M=MI()
    matrix=[]
    for _ in range(N):
        s=sys.stdin.readline().strip()
        matrix.append(s)
    scores=[0]*N
    for j in range(M):
        zero_indices=[idx for idx,strs in enumerate(matrix) if strs[j]=="0"]
        one_indices=[idx for idx,strs in enumerate(matrix) if strs[j]=="1"]
        zero_len=len(zero_indices)
        one_len=len(one_indices)
        if zero_len == 0:
            target=one_indices
        elif one_len == 0:
            target=zero_indices
        elif zero_len < one_len:
            target=zero_indices
        else:
            target=one_indices
        for idx in target:
            scores[idx]+=1
    max_score=max(scores)
    res=[idx+1 for idx,score in enumerate(scores) if score==max_score]
    return res


if __name__ == "__main__":
    res=solver()
    print(*res)

