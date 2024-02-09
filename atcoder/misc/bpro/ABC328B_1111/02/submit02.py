# ライブラリのインポート
import sys
# import heapq,copy
import pprint as pp
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

def solver(M,Days):
    result = 0
    for j in range(1,M+1):
        for k in range(1,Days[j-1]+1):
            fullDate=f"{j}{k}"
            S=set()
            x = len(fullDate)
            for m in range(0,x):
                S.add(fullDate[m])
            slen=len(S)
            if slen==1:
                # xdebug(f"{j}月{k}日はぞろ目です")
                result=result+1
            # xdebug(f"{fullDate}")
    return result


if __name__ == "__main__":
    M=II()
    Days=LI()
    print("{}".format(solver(M,Days)))
