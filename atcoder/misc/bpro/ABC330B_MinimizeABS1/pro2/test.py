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




def solver(N,L,R,Ai):
    result = ""
    baseL=[]
    for j in range(0,N):
        xdebug(f"Aj={Ai[j]}の場合…")
        for Xc in range(L,R+1):
            flug=True
            for Y in range(L,R+1):
                if abs(Xc-Ai[j]) <= abs(Y-Ai[j]):
                    xdebug(f"abs(Xc={Xc}-Aj={Ai[j]})<=abs(Y={Y}-Aj={Ai[j]})を満たす")
                else:
                    xdebug(f"ギョギョ abs(Xc={Xc}-Aj={Ai[j]})>abs(Y={Y}-Aj={Ai[j]})になった")
                    flug=False
            if flug==True:
                xdebug(f"Aj={Ai[j]}の時は {Xc}が条件に満たす")
                xdebug("----------")
                baseL.append(str(Xc))
                break
    # algorithm
    result = " ".join(baseL)
    return result


if __name__ == "__main__":
    N,L,R = MI()
    Ai = LI()
    print("{}".format(solver(N,L,R,Ai)))
