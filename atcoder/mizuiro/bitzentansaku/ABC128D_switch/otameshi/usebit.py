import sys
# from collections import defaultdict
# import heapq,copy
from logging import getLogger, StreamHandler, DEBUG
# import pprint as pp
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

for x in range(100):
    logger.debug("10進数 {} -> 2進数 {}".format(x,bin(x)))
