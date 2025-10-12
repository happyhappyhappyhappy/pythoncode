import os
import sys
import pprint as pp
import unittest

from io import StringIO
from itertools import permutations
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
PERM=permutations

def solver():
    res=False
    resl=[0]
    N=II()
    A=LI()
    for reslr in PERM([j+1 for j in range(N)]):
        resl=list(reslr)
        res1=True
        for k in range(N):
            if not (res1 and (A[k]==-1 or A[k]==resl[k])):
                res1=False
                break
        if res1:
            return res1,resl
    return res,resl

def resolve():
    res,resl=solver()
    if res:
        print("Yes")
        print(*resl)
    else:
        print("No")



class TestClass(unittest.TestCase):
    def test_sample1(self):
        input = """4
-1 -1 2 -1"""
        expected = """Yes
3 1 2 4"""
        self.judge(input, expected)

    def test_sample2(self):
        input = """5
-1 -1 1 -1 1"""
        expected = """No"""
        self.judge(input, expected)

    def test_sample3(self):
        input = """7
3 -1 4 -1 5 -1 2"""
        expected = """Yes
3 7 4 1 5 6 2"""
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
