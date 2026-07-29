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

M=300000
def solver():
    res = 0
    _,m=MI()
    row=[0]*(M+1)
    column=[0]*(M+1)
    rPlace=[0]*(M+1)
    cPlace=[0]*(M+1)
    idx=0
    for j in range(1,m+1):
        row[j],column[j]=MI()
        # xdebug(f"--- No.{j} ({row[j]},{column[j]})---")
        if 0 < rPlace[row[j]]:
            idx=rPlace[row[j]]
            rPlace[row[idx]]=0
            cPlace[column[idx]]=0
            res-=1
            # xdebug(f"({row[idx]},{column[idx]})は取り除かれました 現在 {res}個")
        if 0 < cPlace[column[j]]:
            idx=cPlace[column[j]]
            rPlace[row[idx]]=0
            cPlace[column[idx]]=0
            res-=1
            # xdebug(f"({row[idx]},{column[idx]})は取り除かれました 現在 {res}個")
        rPlace[row[j]]=j
        cPlace[column[j]]=j
        res+=1
        # xdebug(f"({row[j]},{column[j]})に追加されました 現在 {res}個")
    return res

if __name__ == "__main__":
    res=solver()
    print(res)
