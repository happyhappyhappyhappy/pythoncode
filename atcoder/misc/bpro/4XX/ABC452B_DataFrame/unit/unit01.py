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
def SI(): return input().rstrip()
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
    H,W=MI()
    G=[]
    for _ in range(H):
        lineList=[]
        lineList.append("#")
        for _ in range(W-2):
            lineList.extend(".")
        lineList.append("#")
        G.append(lineList)
    for j in range(W):
        G[0][j]="#"
    for j in range(W):
        G[H-1][j]="#"
    return G

def resolve():
    res=solver()
    for line in res:
        joinStr="".join(line)
        print(joinStr)



class TestClass(unittest.TestCase):
    def test_sample1(self):
        input = """4 5"""
        expected = """#####
#...#
#...#
#####"""
        self.judge(input, expected)

    def test_sample2(self):
        input = """5 6"""
        expected = """######
#....#
#....#
#....#
######"""
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
