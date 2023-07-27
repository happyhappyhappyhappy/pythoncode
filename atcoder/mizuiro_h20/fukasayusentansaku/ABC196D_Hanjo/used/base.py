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

H,W,A,B = MI()
ans = 0
def dfs(j,bit,A,B):
    xdebug("ただいま,dfs({},{},{},{})に入りました"
           .format(j,bit,A,B))
    if j == H*W:
        global ans
        ans = ans+1
        xdebug("条件{}=={}*{}になったので回答を一つ加えて再帰終了"
               .format(j,H,W))
        return
    if bit >> j & 1:
        xdebug("{} >> {} & 1 を満たすので".format(bit,j))
        xdebug("dfs({},{},{},{})の再帰実行".format
               (j+1,bit,A,B))
        dfs(j+1,bit,A,B)
        return
    if B:
        dfs(j+1,bit|1<<j,A,B-1)
    if A:
        if j % W != W - 1 and not bit & 1 << (j+1):
            dfs(j+1,bit|1<<j|1<<(j+1),A-1,B)
        if (j + W) < (H * W):
            dfs(j+1,bit|1<<j|1<<(j+W),A-1,B)
dfs(0,0,A,B)
print(ans)
