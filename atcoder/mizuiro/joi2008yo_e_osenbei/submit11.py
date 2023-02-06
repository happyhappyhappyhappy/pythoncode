# あくまで2回のひっくり返し処理を行わないだけの場合(模範解答の写しではない)
import sys
# from collections import defaultdict
import copy
from itertools import product
import pprint as pp
# from collections import deque
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]
xprint=pp.pprint

# Const
MAXSIZE = ( 1 << 31 ) -1
MINSIZE = -( 1 << 31) + 1

def showG(R,C,G):
    for j in range(0,R):
        print(G[j])

def solver(R,C,bit,G):
    result = 0
    print("bit = {} 変更前".format(bit))
    showG(R,C,G)
    for j in range(0,R):
        if bit[j] == 1:
            for k in range(0,C):
                G[j][k] = (G[j][k]+1)%2
    # algorithm
    print("bit = {} 変更後".format(bit))
    showG(R,C,G)
    # TODO: 各列に対して1になっている個数を数え、ここからRを使って0の値を求める
    # 最大をresultに足す
    return result

def chmax(x,y):
    if x < y:
        x = y
    return x

if __name__ == "__main__":
    R,C = MI()
    Gorg = list()
    print("R = {} , C = {}".format(R,C))
    for j in range(0,R):
        Gorg.append(LI())
    xprint(Gorg)
    bits = product((0,1),repeat=R)
    answer = 0
    for bit in bits:
        G = copy.deepcopy(Gorg)
        subans = solver(R,C,bit,G)
        chmax(answer,subans)
    print("{}".format(answer))
