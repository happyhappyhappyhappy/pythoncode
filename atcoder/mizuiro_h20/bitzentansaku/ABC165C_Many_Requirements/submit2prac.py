# ライブラリのインポート
import sys
# import heapq,copy
import pprint as pp
# from collections import deque
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
# Const
MAXSIZE = ( 1 << 59 ) -1
MINSIZE = -( 1 << 59) + 1

N,M,Q = MI()
F=LLI(Q)

a=[]
b=[]
c=[]
d=[]

# xdebug(F)

for x in range(0,Q):
    a.append(F[x][0]-1)
    b.append(F[x][1]-1)
    c.append(F[x][2])
    d.append(F[x][3])

# xdebug("どこから = {}".format(a))
# xdebug("どこまで = {}".format(b))
# xdebug("この差ならば = {}".format(c))
# xdebug("この点が与えられる = {}".format(d))
def score(A):
    ans=0
    for x in range(0,Q):
            dif = 0
            bn = b[x]
            an = a[x]
            dif = A[bn]-A[an]
            # xdebug("差は {}".format(dif))
            if dif == c[x]:
                ans=ans+d[x]
    return ans

def dfs(C,A):
    # xdebug("ただいま {}".format(A))
    if C == N:
        # xdebug("{} と {}個の列 到達したので点数を求める\n".format(A,N))
        return score(A)
    else:
        ans = 0
        lastnum=-1 # 一応初期化をしておく
        if C == 0:
            lastnum = 1 # 最初の場合はまずこれからセット
        else:
            lastnum = A[C-1]
        for x in range(lastnum,M+1):
            now_ans=0
            A.append(x)
            now_ans=dfs(C+1,A)
            # xdebug("ans={},now_ans={}".format(ans,now_ans))
            ans = max(ans,now_ans)
            A.pop()
        return ans


print(dfs(0,[]))
