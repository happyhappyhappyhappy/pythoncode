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
    res = []
    _,_=MI()
    TAKA=input()
    AO=input()
    Q=II()
    CHK_STR=[]
    for _ in range(Q):
        tmp=input()
        CHK_STR=[*CHK_STR,tmp]
    for CHK in CHK_STR:
        takaFlug=True
        aoFlug=True
        for chkChar in CHK:
            if chkChar not in TAKA:
                takaFlug=False
            if chkChar not in AO:
                aoFlug=False
        if takaFlug is True and aoFlug is False:
            res=[*res,"Takahashi"]
        elif takaFlug is False and aoFlug is True:
            res=[*res,"Aoki"]
        else:
            res=[*res,"Unknown"]
    return res


if __name__ == "__main__":
    res=solver()
    for x in res:
        print(x)
