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

def yamapow1(p:int,n:int)->int:
    res=1
    while 0 < n:
        nand1=n&1
        if nand1 == 1:
            res=res*p
        p=p*p
        n=n>>1
    return res

def solver():
    res=0
    N,M=MI()
    THISMAX=yamapow1(10,9)
    for j in range(M+1):
        x=yamapow1(N,j)
        res=res+x
        if THISMAX < res:
            return "inf"
    return res

def resolve():
    print(solver())

class TestClass(unittest.TestCase):
    def test_sample1(self):
        input = """7 3"""
        expected = """400"""
        self.judge(input, expected)

    def test_sample2(self):
        input = """1000000 2"""
        expected = """inf"""
        self.judge(input, expected)

    def test_sample3(self):
        input = """999999999 1"""
        expected = """1000000000"""
        self.judge(input, expected)

    def test_sample4(self):
        input = """998244353 99"""
        expected = """inf"""
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
