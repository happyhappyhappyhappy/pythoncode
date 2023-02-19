from logging import getLogger, StreamHandler, DEBUG
import sys
from collections import defaultdict,Counter
from itertools import product
import heapq,copy
import pprint as pp
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]
logger = getLogger(__name__)
handler = StreamHandler()
handler.setLevel(DEBUG)
logger.setLevel(DEBUG)
logger.addHandler(handler)
logger.propagate = False
xdebug=logger.debug
xprint=pp.pprint
# Const
## MAXSIZE = ( 1 << 31 ) -1
MAXSIZE =  1 << 60
MINSIZE = -( 1 << 31) + 1

def chmin(A,B):
    if A > B:
        A =B

def minSum(N,K,Ai,cList):
    resCost = 0
    # algorithm
    nowMin = Ai[0]
    for pos in range(1,N):
        if cList[pos] == 1:
#            xdebug("{} : このビルの色が見える様にする".format(pos))
            if Ai[pos] <= nowMin:
#                xdebug("Ai[{}] <= {} = nowMinなので桁上げする".\
#                   format(pos,nowMin))
                plusCost=(nowMin+1)-Ai[pos]
                resCost=resCost+plusCost
#                xdebug("現在のコスト:{}".format(resCost))
                nowMin=Ai[pos]+plusCost
        nowMin = max(Ai[pos],nowMin)
#    xdebug("選択={} 時の最終コスト={}".format(cList,resCost))
    return resCost


if __name__ == "__main__":
    N,K = MI()
    A_LIST=LI()
    # xdebug(A_LIST)
    answer=MAXSIZE
    for lists in product([0,1],repeat=N):

        if lists[0] == 0:
            continue
        oneC = Counter(lists)
        if oneC[1] != K:
            continue
        C_LIST=copy.deepcopy(A_LIST)
        xans=minSum(N,K,C_LIST,lists)
        answer=min(answer,xans)
#        xdebug(C_LIST)
    print("{}".format(answer))
