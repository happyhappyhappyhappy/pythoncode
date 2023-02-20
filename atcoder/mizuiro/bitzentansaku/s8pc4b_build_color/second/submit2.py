# ライブラリのインポート
import sys
import pprint as pp
from collections import Counter
from itertools import product
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

# 上から下へと行ってみる

N,K = MI()
A = LI()

answer = MAXSIZE
for SL in product([0,1] , repeat=N):
    cnt=Counter(SL)
    if cnt[1] != K:
        continue
    if SL[0] != 1:
        continue
    costmin=0
    maxbuild=A[0]
    for x in range(1,N):
        if SL[x] == 1:
            if A[x] <= maxbuild:
                nowcost = maxbuild+1-A[x]
                costmin = costmin+nowcost
                maxbuild=maxbuild+1
        maxbuild=max(maxbuild,A[x])
    answer=min(costmin,answer)
print(answer)
