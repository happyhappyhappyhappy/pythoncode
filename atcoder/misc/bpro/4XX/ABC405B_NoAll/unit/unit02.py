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
    N,M=MI()
    answer=N
    Analyze_List=LI()
    for cut_size in range(N):
        Box=[False]*(M+1)
        list_length=len(Analyze_List)
        for list_pos in range(list_length):
            Box[Analyze_List[list_pos]]=True
        for box_pos in range(1,M+1):
            if Box[box_pos] is False:
                return cut_size
        Analyze_List=Analyze_List[:-1]
    return answer

def resolve():
    answer=solver()
    print(answer)

class TestClass(unittest.TestCase):
    def test_sample1(self):
        input = """5 3
3 2 3 1 2"""
        expected = """2"""
        self.judge(input, expected)

    def test_sample2(self):
        input = """4 3
1 3 1 3"""
        expected = """0"""
        self.judge(input, expected)

    def test_sample3(self):
        input = """10 4
1 3 3 4 2 1 3 1 2 4"""
        expected = """6"""
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
