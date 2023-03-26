# ライブラリのインポート
import sys
import copy
import pprint as pp
from collections import deque
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

dwdh_odd=[
    (1,-1), # 0:00-2:00
    (1,0), # 2:00-4:00
    (1,1), # 4:00-6:00
    (0,1), # 6:00-8:00
    (-1,0), # 8:00-10:00
    (0,-1) # 10:00-12:00
]
dwdh_even=[
    (0,-1), # 0:00-2:00
    (1,0), # 2:00-4:00
    (1,1), # 4:00-6:00
    (-1,1), # 6:00-8:00
    (-1,0), # 8:00-10:00
    (-1,-1) # 10:00-12:00
]

def solver():
    result = 0
    # algorithm
    return result

def ShowG(G,H):
    for h in range(0,H):
        xdebug(G[h])

if __name__ == "__main__":
    W,H=map(int,input().split())
    G=[]
    G.append([0]*(W+2))
    for h in range(0,H):
        S = list(LI())
        # xdebug("{} 行目に {} を入れたい".format(h,S))
        G.append([0]+S+[0])
    G.append([0]*(W+2))
    ShowG(G,H+2)
    # print("{}".format(solver()))
    V = [[0] * (W+2) for h in range(H+2) ]
    for h in range(H+2):
        xdebug(V[h])
    answer =0
#    Q = deque()
    Q = deque([])
    Q.append([0,0])
    while len(Q)!= 0 :
        DQ = Q.popleft()
        h = DQ[0]
        w = DQ[1]
        if V[h][w] == 1:
            continue
        else :
            xdebug("({},{})に訪問済みのフラグを立てました".format(h,w))
            V[h][w] = 1
            if h%2 == 1:
                dwdh = dwdh_odd
            else :
                dwdh = dwdh_even
            for dw,dh in dwdh:
                nextw = w+dw
                nexth = h+dh
                if (0 <= nextw < W+2 )and (0 <= nexth < H+2):
                    if G[nexth][nextw] == 1:
                        xdebug("({},{})に衝突しました".format(nexth,nextw))
                        answer = answer+1
                        xdebug(answer)
                    else:
                        if V[nexth][nextw] == 0:
                            Q.append([nexth,nextw])
    print(answer)
