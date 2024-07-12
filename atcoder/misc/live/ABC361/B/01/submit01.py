# ライブラリのインポート
# import heapq,copy
import pprint as pp
import sys

# from collections import deque
# pypy3用
# import pypyjit
# 再帰制御解放
# pypyjit.set_param('max_unroll_recursion=-1')
# sys.setrecursionlimit(10**6)
from logging import DEBUG, StreamHandler, getLogger

# 入力のマクロ
def II(): return int(sys.stdin.readline())
def SI(): return sys.stdin.readline().strip()
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number:int): return [LI() for _ in range(rows_number)]

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

def unit(a,b,c,d):
    ans=False
    # xdebug(f"{axis}軸 [{a},{b}][{c},{d}]の調査をします")
    if not(b <= c or d <= a):
        # xdebug(f"{axis}軸 [{a},{b}]と[{c},{d}]は重なっています O")
        ans=True
    return ans

def solver():
    result = "No"
    # algorithm
    x1,y1,z1,x2,y2,z2=MI()
    x3,y3,z3,x4,y4,z4=MI()
    # xdebug("与えられた各軸の情報")
    # xdebug(f"X軸 [{x1},{x2}]と[{x3},{x4}]")
    # xdebug(f"Y軸 [{y1},{y2}]と[{y3},{y4}]")
    # xdebug(f"Z軸 [{z1},{z2}]と[{z3},{z4}]")
    # xunit=unit("X",x1,x2,x3,x4)
    # yunit=unit("Y",y1,y2,y3,y4)
    # zunit=unit("Z",z1,z2,z3,z4)
    if unit(x1,x2,x3,x4) and unit(y1,y2,y3,y4) and unit(z1,z2,z3,z4):
#        xdebug("全部の軸で重なっています")
        result="Yes"
    # else:
    #     xdebug("一つ以上の軸で重なっていません")
    return result


if __name__ == "__main__":
    print(solver())
