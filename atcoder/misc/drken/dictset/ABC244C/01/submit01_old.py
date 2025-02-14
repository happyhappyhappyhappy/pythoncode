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

def countTrue(box):
    ln=len(box)
    cnt=0
    for j in range(ln):
        if box[j] is True:
            cnt+=1
    return cnt

def tkhsdecline(boxes,MX):
    for j in range(1,MX+1):
        if boxes[j] is False:
            boxes[j]=True
            # xdebug(f"boxes:{boxes}")
            # xdebug(f"j:{j}")
            return boxes,j


def solver():
    # algorithm
    N=II()
    MX=2*N+1
    box=[False]*(MX+1)
    while True:
        box,tkhs_say=tkhsdecline(box,MX)
        xdebug(f"宣言:{tkhs_say},box:{box}")
        print(tkhs_say,flush=True)
        T=II()
        xdebug(f"もらう:{T}")
        box[T]=True
        if T == 0:
            xdebug("終わり")
            break

if __name__ == "__main__":
    solver()
