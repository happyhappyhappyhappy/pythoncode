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

def solver(W,X):
    result = 0
    N=len(W)
    cnt=[0]*24
    for j in range(0,N):
        jst=X[j]
        cnt[jst]=cnt[jst]+W[j]
    # for j in range(0,24):
    #     xdebug(f"基準時間 {j}->{cnt[j]}人")
    for j in range(0,24): # 現地の0時を標準のjとした場合の組み合わせ
        nowTotal=0
        for k in range(9,18): # 標準0時基準の会議設定時間
            nowTotal=nowTotal+cnt[(j+k)%24]
        if result < nowTotal:
            # xdebug(f"現地0を標準{j}の場合->{(j+9)%24}から{(j+17)%24} {nowTotal}")
            result=nowTotal
    # algorithm
    # for j in range(0,24):
    #     sttime=[]
    #     nowTotal=0
    #     for k in range(9,18):
    #         sttime.append(((j+k)%24))
    #     tzone=" ".join(map(str,sttime))
    #     xdebug(f"標準{j}時を現地0時とした場合 で9-17startの組->{tzone}")
    return result

if __name__ == "__main__":
    N=II()
    W=[]
    X=[]
    for _ in range(0,N):
        w,x=MI()
        W.append(w)
        X.append(x)
    print("{}".format(solver(W,X)))
