# ライブラリのインポート
import sys
import pprint as pp
# pypy3用
import pypyjit
# 再帰制御解放
pypyjit.set_param('max_unroll_recursion=-1')
sys.setrecursionlimit(10**6)
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


def dfs(A):
    xdebug("Now A:{}".format(A))
    global ans
    # 数列の長さが N に達したら計算

    if len(A) == N:
        xdebug("A {} の長さが {} になったので計算開始\n".format(A,len(A)))
        score = 0
        for i in range(Q):
            if A[L[i][1]-1]-A[L[i][0]-1]==L[i][2]:
                score += L[i][3]
        ans = max(ans,score)
        return
    xdebug("A[-1]={}".format(A[-1]))
    for v in range(A[-1],M+1):
        dfs(A+[v])

N,M,Q = map(int, input().split())
L = []
for i in range(Q):
    L.append(list(map(int, input().split())))
ans = 0
dfs([1])
print(ans)
