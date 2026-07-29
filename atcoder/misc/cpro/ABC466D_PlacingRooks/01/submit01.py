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
N=300000
M=300000


def solver():
    res = 0
    _,m=MI()
    row=[0]*(N+1)
    column=[0]*(N+1)
    rowPlace=[0]*(N+1)
    columnPlace=[0]*(N+1)
    for j in range(1,m+1):
        # xdebug(f"----- Turn No.{j} -----")
        row[j],column[j]=MI()
        # xdebug(f"({row[j]},{column[j]})を置きます")
        if rowPlace[row[j]]!=0:
            idx=rowPlace[row[j]]
            rowPlace[row[idx]]=0
            columnPlace[column[idx]]=0
            res-=1
            # xdebug(f"列が上書きされ ({row[idx]},{column[idx]})が取り除かれました 現在 {res}")
        if columnPlace[column[j]]!=0:
            idx=columnPlace[column[j]]
            rowPlace[row[idx]]=0
            columnPlace[column[idx]]=0
            res-=1
            # xdebug(f"行が上書きされ ({row[idx]},{column[idx]})が取り除かれました 現在 {res}")
        res+=1
        columnPlace[column[j]]=j
        rowPlace[row[j]]=j
        # xdebug(f"({row[j]},{column[j]})が追加されました 現在 {res}")
    return res


if __name__ == "__main__":
    res=solver()
    print(res)
