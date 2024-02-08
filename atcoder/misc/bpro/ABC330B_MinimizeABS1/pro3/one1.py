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

N,L,R=MI()
A=LI()
X=L
Res=[]
for a in A:
    print(f"{a}の場合")
    for x in range(L,R+1):
        print(f"まずx={x}を考える")
        flag=True
        for Y in range(L,R+1):
            if abs(x-a) > abs(Y-a):
                print(f"abs(x={x}-a={a} > abs(Y={Y}-a={a}))が発生。このxはダメ!!")
                flag=False
                break
            else:
                print(f"abs(x={x}-a={a} <= abs(Y={Y}-a={a}))にて問題出ない")
        if flag==True:
            print(f"x={x}で関門通過。a={a}のときはこれが答え")
            Res.append(x)
            break
outRes=" ".join(map(str,Res))
print(outRes)
