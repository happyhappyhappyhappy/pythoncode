# Problem:
# Python  Try

import sys
import numpy as np
# from collections import defaultdict
# import heapq,copy
# import pprint as pp
# from collections import deque
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]


# Const
MAXSIZE = ( 1 << 31 ) -1
MINSIZE = -( 1 << 31) + 1
# PLOTSIZE = 5000

# PLOT : 方眼変数 出力しないこと
# PLOT=np.array([[False for j in range(PLOTSIZE)] for k in range(PLOTSIZE)])
# ColPLOT : 柱がある位置: setオブジェクトに変更
ColPlOT = set()

def isPoint(P1):
    [x,y] = P1
    if P1 in ColPlOT:
        return True
    else:
        return False

def get_area(p1,p2):
    [x1,y1] = p1
    [x2,y2] = p2
    p3 = [x2+y1-y2,y2+x2-x1]
    p4 = [x1+y1-y2,y1+x2-x1]
    if isPoint(p3) and isPoint(p4):
        return pow(x2-x1,2)+pow(y2-y1,2)
    return 0

def solver(n,point):
    ans_area=0
    point.sort()
    for j in range(n):
        ColPlOT.add(point[j])
    for j in range(n):
        [x,y] = point[j]
    for j in range(n):
        for k in range(j+1,n):
            p1 = point[j]
            p2 = point[k]
            ans_area = max(ans_area,get_area(p1,p2))
    return ans_area

if __name__ == "__main__":

    PointCnt = II()
    Point = LLI(PointCnt)

    print("{}".format(solver(PointCnt,Point)))
