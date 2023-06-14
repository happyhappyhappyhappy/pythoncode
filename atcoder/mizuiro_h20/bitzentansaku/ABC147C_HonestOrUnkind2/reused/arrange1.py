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




def solver(N,L):
    res = 0
    for t in range(0,N):
        xdebug("{} さんの発言".format(t))
        B = len(L[t]) # t氏の情報長さ
        for s in range(0,B):
            xdebug("{}番目".format(s+1))
            x,y = L[t][s]
            saidStr=""
            if y==1 :
                saidStr="正直者"
            else:
                saidStr="うそつき"
            xdebug("{} さんは {}です".format(x,saidStr))
    # algorithm
    for j in range(0,2**N):
        kindersdata=[]
        for k in range(0,N):
            kindflg=(j>>k)&1
            if kindflg==1:
                kindersdata.append(1)
            else :
                kindersdata.append(0)
        xdebug("親切チェーン :{}".format(kindersdata))
        flag = True
        for k in range(0,N):
            if kindersdata[k]==1:
                xdebug("{} さんが親切だと仮定します".format(k))
                for x,y in L[k]:
                    if kindersdata[x]!=y:
                        xdebug("入力データ {} さんは {}である→不一致".format(kindersdata[x],y))
                    else :
                        xdebug("入力データ {} さんは {}です→一致".format(kindersdata[x],y))
    return res


if __name__ == "__main__":
    # 人数N
    N = II()
    # 各自の情報テーブル
    L = [[] for _ in range(0,N)]
    for j in range(0,N):
        # 発言数A
        A = II()
        for _ in range(0,A):
            x,y=MI()
            L[j].append([x-1,y])
    print("{}".format(solver(N,L)))
