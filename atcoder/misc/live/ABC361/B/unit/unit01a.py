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

def unit(a,b,c,d):
    ans=False
    if not(b <= c or d <= a):
        ans=True
    return ans

def solver():
    ans="No"
    x1,y1,z1,x2,y2,z2=MI()
    x3,y3,z3,x4,y4,z4=MI()
    if unit(x1,x2,x3,x4) and unit(y1,y2,y3,y4) and unit(z1,z2,z3,z4):
        ans="Yes"
    return ans

def resolve():
    print(solver())

class TestClass(unittest.TestCase):
    def test_sample1(self):
        input = """0 0 0 4 5 6
2 3 4 5 6 7"""
        expected = """Yes"""
        self.judge(input, expected)

    def test_sample2(self):
        input = """0 0 0 2 2 2
0 0 2 2 2 4"""
        expected = """No"""
        self.judge(input, expected)

    def test_sample3(self):
        input = """0 0 0 1000 1000 1000
10 10 10 100 100 100"""
        expected = """Yes"""
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
