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

N,M,K,S = MI()
nMotel,zMotel=MI()
ZONBIE=[]
for _ in range(0,K):
    z = II()
    ZONBIE.append(z-1)
# リンクセット取得
LINKS=[]
for _ in range(0,M):
    a,b=MI()
    LINKS.append([a-1,b-1])
    LINKS.append([b-1,a-1])
print(f"ルート {LINKS}")
zDist=[MAXSIZE]*N
q=deque(ZONBIE)
for v in ZONBIE:
    zDist[v]=0
while len(q)!=0:
    node = q.popleft()
    for next_city in LINKS[]
