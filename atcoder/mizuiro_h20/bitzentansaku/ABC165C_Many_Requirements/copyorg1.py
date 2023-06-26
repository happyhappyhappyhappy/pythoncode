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
# Const
MAXSIZE = ( 1 << 59 ) -1
MINSIZE = -( 1 << 59) + 1

def chmin(x,y):
    xdebug("x ({}) = {}".format(id(x),x))
    xdebug("y ({}) = {}".format(id(y),y))
    if x > y:
        x = y
        xdebug("C_After : x ({}) = {}".format(id(x),x))
        xdebug("C_After : y ({}) = {}".format(id(y),y))



def solver(N,M,Q,a,b,c,d):
    result = 0

    # algorithm
    return result


if __name__ == "__main__":
    N,M,Q=MI()
    a=[]
    b=[]
    c=[]
    d=[]
    for j in range(0,Q):
        ap,bp,cp,dp=MI()
        a.append(ap)
        b.append(bp)
        c.append(cp)
        d.append(dp)
    print("{}".format(solver(N,M,Q,a,b,c,d)))
