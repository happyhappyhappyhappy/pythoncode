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



def algofunc(d,q,r):
    """
        d:ゴミの提出日
        q:ゴミの回収周期
        r:回収周期+余りの所
    """
    res=0
    dr=d-r # まず余り分を引いて評価する
    age=(dr+(q-1))//q # drの結果を切り上げする
    r0=age*q # もしrが0の場合の回収日を求める
    res=r0+r
    return res
def solver():
    """
        回答を書くところ
    """
    result = 0
    N=II()
    gcdata=list()
    for _ in range(N):
        q,r=MI()
        gcdata.append((q,r))
    xdebug(f"{gcdata}")
    result=list()
    Q=II()
    for _ in range(Q):
        pat,d=MI()
        q,r=gcdata[pat-1]
        x=algofunc(d,q,r)
        result.append(x)
    # algorithm
    return result


if __name__ == "__main__":
    reslist=solver()
    reslen=len(reslist)
    for j in range(reslen):
        print(reslist[j])
