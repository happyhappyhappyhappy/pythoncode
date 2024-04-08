import os
import sys
import pprint as pp
import unittest

from collections import defaultdict
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
    N=II()
    beans=defaultdict(int)
    for _ in range(N):
        sweet,color=MI()
        if color in beans:
            if sweet < beans[color]:
                beans[color]=sweet
        else:
            beans[color]=sweet
    ans=0
    for value in beans.values():
        if ans < value:
            ans=value
    return ans

def resolve():
    print(solver())

class TestClass(unittest.TestCase):
    def test_sample1(self):
        input = """4
100 1
20 5
30 5
40 1"""
        expected = """40"""
        self.judge(input, expected)

    def test_sample2(self):
        input = """10
68 3
17 2
99 2
92 4
82 4
10 3
100 2
78 1
3 1
35 4"""
        expected = """35"""
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
