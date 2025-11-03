# ライブラリのインポート
# import heapq,copy
import pprint as pp
import sys
from typing import Tuple,List

from logging import DEBUG, StreamHandler, getLogger

def MI()->Tuple[int,...]:
    return map(int,sys.stdin.readline().split())
# 入力のマクロ
def II(): return int(sys.stdin.readline())
def SI(): return sys.stdin.readline().strip()
# def MI(): return map(int, sys.stdin.readline().split())
def LI()->List[int]:
    return list(MI())
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


def solver():
    _,M=MI()
    A=LI()
    sum_A=sum(A)
    target_number=sum_A-M
    if target_number in A:
        return "Yes"
    else:
        return "No"

if __name__ == "__main__":
    res=solver()
    print(res)
