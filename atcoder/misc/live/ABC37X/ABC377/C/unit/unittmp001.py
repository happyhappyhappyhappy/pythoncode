import os
import sys
import pprint as pp
import unittest

from io import StringIO

# ライブラリのインポート
# import heapq,copy

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

def solver():
    res2=0
    N,M=MI()
    avoidPos=set()
    kingPos=[]
    for _ in range(M):
        ln,rw = MI()
        avoidPos.add((ln,rw))
        kingPos.append([ln,rw])
    d=[[2,1],[1,2],[-1,2],[-2,1],
    [-2,-1],[-1,-2],[1,-2],[2,-1]]
    xdebug(f"avoidPos={avoidPos}")
    xdebug(f"kingPos={kingPos}")
    xdebug(f"方向={d},数={len(d)}")
    for j in range(M):
        kingln,kingrw=kingPos[j]
        for k in range(8):
            [dln,drw]=d[k]
            xdebug(f"({dln},{drw})")
            newln=dln+kingln
            newrw=drw+kingrw
            if 1 <= newln and newln <= N and 1 <= newrw and newrw <= N:
                avoidPos.add((newln,newrw))
    xdebug(f"結果危険箇所 : {len(avoidPos)}")
    res=N*N-len(avoidPos)
    xdebug(f"答えは{res}")
    return res

def resolve():
    print(solver())

class TestClass(unittest.TestCase):
    def test_sample1(self):
        input = """8 6
1 4
2 1
3 8
4 5
5 2
8 3"""
        expected = """38"""
        self.judge(input, expected)

    def test_sample2(self):
        input = """1000000000 1
1 1"""
        expected = """999999999999999997"""
        self.judge(input, expected)

    def test_sample3(self):
        input = """20 10
1 4
7 11
7 15
8 10
11 6
12 5
13 1
15 2
20 10
20 15"""
        expected = """338"""
        self.judge(input, expected)

    def judge(self, input, expected):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        actual = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(expected, actual)

if __name__ == "__main__":
    if "ATCODER" in os.environ:
        resolve()
    else:
        unittest.main(verbosity=2)
