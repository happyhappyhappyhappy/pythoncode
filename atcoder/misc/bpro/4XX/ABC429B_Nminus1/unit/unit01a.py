import os
import sys
import pprint as pp
import unittest
from typing import List,Tuple

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

def MI() -> Tuple[int,...]:
    return map(int,sys.stdin.readline().split())
def LI() -> List[int]:
    return list(MI())

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
    _,M=MI()
    A:List[int]=LI()
    sum_A=sum(A)
    target_number=sum_A-M
    if target_number in A:
        return "Yes"
    else:
        return "No"

def resolve():
    res=solver()
    print(res)



class TestClass(unittest.TestCase):
    def test_sample1(self):
        input = """4 10
3 2 3 4"""
        expected = """Yes"""
        self.judge(input, expected)

    def test_sample2(self):
        input = """5 16
3 3 4 2 5"""
        expected = """No"""
        self.judge(input, expected)

    def test_sample3(self):
        input = """6 16
0 8 0 2 6 8"""
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
