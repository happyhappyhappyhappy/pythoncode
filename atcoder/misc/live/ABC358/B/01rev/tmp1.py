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
    result=[0]
    N,A=MI()
    T=LI()
    for j in range(len(T)):
        xdebug(f"{j+1}->{T[j]}")
    return result

def resolve():
    result=solver()
    for r in result:
        print(r)

class TestClass(unittest.TestCase):
    def test_sample1(self):
        input = """3 4
0 2 10"""
        expected = """4
8
14"""
        self.judge(input, expected)

    def test_sample2(self):
        input = """3 3
1 4 7"""
        expected = """4
7
10"""
        self.judge(input, expected)

    def test_sample3(self):
        input = """10 50000
120190 165111 196897 456895 540000 552614 561627 743796 757613 991216"""
        expected = """170190
220190
270190
506895
590000
640000
690000
793796
843796
1041216"""
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
