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

H,W,A,B = MI()
used=[[0 for _ in range(0,W+1)] for _ in range(0,H+1)]
def dfs(x,y,a):
    xdebug("現在({},{}) A の保持数 {}".format(x,y,a))
    xdebug("中身")
    ppp(used)
    # 初期条件処理
    # 座標(x,y)に置き場所があり、現在所有の長方形畳がa枚ある
    if y == H:# 最後まで到着
        xdebug("枠外 ({},{})へ来ました".format(x,y))
        xdebug("残りのAは{}枚です".format(a))
        if a==0:
            xdebug("回答が1つ増えます")
            return 1 # 長方形の畳を全部使っていれば1通りと返す
        else:
            xdebug("余ってしまったため失敗")
            return 0 # 余ってしまった場合は除外
    if x == W: # 右端まで到着→次の行の先頭へ行く
        xdebug("({},{})と右端へ来ましたので({},{})へ飛びます"
               .format(x,y,0,y+1))
        return dfs(0,y+1,a)
    if used[y][x] == 1: # 使用済み
        xdebug("({},{})は使われているので次({},{})へ進みます"
               .format(x,y,x+1,y))
        return dfs(x+1,y,a) # 無視して右の置き場へ
    r1=0
    r2=0
    r3=0
    # 分散処理開始
    # 右方向に置く場合
    xdebug("({},{})から右に置く場合".format(x,y))
    xdebug("x+1={}".format(x+1))
    if (x+1 < W) and (used[y][x+1]==0) and (0<a):
        used[y][x]=1
        used[y][x+1]=1
        r1=dfs(x+1,y,a-1)
        xdebug("おいて次のマスへ行く場合={}".format(r1))
        # 次の場合に備えて一旦クリア
        used[y][x]=0
        used[y][x+1]=0
    # 下方向に置く場合
    if (0<a) and (y+1<H) and (used[y+1][x]==0):
        used[y][x]=1
        used[y+1][x]=1
        r2=dfs(x+1,y,a-1)
        used[y][x]=0
        used[y+1][x]=0
    # ここには置かない場合
        r3=dfs(x+1,y,a)
        xdebug("縦置き {} パターン,横置き {}パターン,置かない {}パターン"
               .format(r1,r2,r3))
    return r1+r2+r3

ans=dfs(0,0,A)
print(ans)
