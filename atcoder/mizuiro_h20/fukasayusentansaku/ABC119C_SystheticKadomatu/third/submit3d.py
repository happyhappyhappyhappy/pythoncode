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

N,A,B,C=MI()
lList = []
for _ in range(0,N):
    x = II()
    lList.append(x)

def dfs(a,b,c,now_pos):
    if now_pos == N:
        # くっつけることはできたので後は長さの操作
        minpos = min(a,b,c)
        # もし くっつけたことを踏まえても0しかなければ、もはや長さの操作はできないので最大数を返す
        if minpos == 0:
            return MAXSIZE
        else:
            # 長さ調整に利用する魔法の量は各完成物から目標との差を絶対値
            # 最後の10*3は始めて棒をセットするときは合成魔法は要らないので
            # その分を消した
            useMagic = abs(a-A)+abs(b-B)+abs(c-C)-(10*3)
            return useMagic
    else:
        # now_pos番目の竹を取り付けていく
        # Aの場合
        minPoint1 = dfs(a+lList[now_pos],b,c,now_pos+1)+10
        # Bの場合
        minPoint2 = dfs(a,b+lList[now_pos],c,now_pos+1)+10
        # Cの場合
        minPoint3 = dfs(a,b,c+lList[now_pos],now_pos+1)+10
        # 使わない場合
        minPoint4 = dfs(a,b,c,now_pos+1)
        now_min = min(minPoint1,minPoint2,minPoint3,minPoint4)
        return now_min

ans = dfs(0,0,0,0)
print(ans)
