from logging import getLogger, StreamHandler, DEBUG
import sys
from collections import defaultdict
from itertools import product
import heapq,copy
import pprint as pp
# from collections import deque
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
logger.debug('デバッグの例')
xdebug=logger.debug

# Const
MAXSIZE = ( 1 << 31 ) -1
MINSIZE = -( 1 << 31) + 1


def solver(N,K,Ai):
    result = 0
    for x in product([0,1],repeat=N):
        xdebug(x)
        dictk = defaultdict(x)
        xdebug(dictk)
    # algorithm
    return result


if __name__ == "__main__":
    N,K = MI()
    A_LIST=LI()
    xdebug(A_LIST)
    print("{}".format(solver(N,K,A_LIST)))
