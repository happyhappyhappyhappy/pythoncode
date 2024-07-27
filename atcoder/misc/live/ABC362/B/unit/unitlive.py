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
    ans="No"
    ax,ay=MI()
    bx,by=MI()
    cx,cy=MI()
    ab2=pow((ax-bx),2)+pow((ay-by),2)
    ac2=pow((ax-cx),2)+pow((ay-cy),2)
    bc2=pow((cx-bx),2)+pow((cy-by),2)
    xdebug(f"ab2={ab2},ac2={ac2},bc2={bc2}")
    hen=[0 for _ in range(3)]
    hen[0]=ab2
    hen[1]=ac2
    hen[2]=bc2
    hen.sort()
    xdebug(f"辺={hen}")
    if hen[0]+hen[1] == hen[2]:
        ans="Yes"
    return ans

def resolve():
    print(solver())

class TestClass(unittest.TestCase):
    def test_sample1(self):
        input = """0 0
4 0
0 3"""
        expected = """Yes"""
        self.judge(input, expected)

    def test_sample2(self):
        input = """-4 3
2 1
3 4"""
        expected = """Yes"""
        self.judge(input, expected)

    def test_sample3(self):
        input = """2 4
-3 2
1 -2"""
        expected = """No"""
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
