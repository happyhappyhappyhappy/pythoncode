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
    ans=["No","0"]
    N=II()
    LList=[0 for _ in range(N)]
    RList=[0 for _ in range(N)]
    for j in range(N):
        lpos,rpos=MI()
        LList[j]=lpos
        RList[j]=rpos
    xdebug(f"N={N},L={LList},R={RList}")
    sumX=sum(LList)
    xdebug(f"sum={sumX}")
    if sum(LList) < 0 or sum(RList) < 0:
        return ans
    return ans

def resolve():
    ans=solver()
    print(ans[0])
    if ans[0] == "Yes":
        print(ans[1])

class TestClass(unittest.TestCase):
    def test_sample1(self):
        input = """3
3 5
-4 1
-2 3"""
        expected = """Yes
4 -3 -1"""
        self.judge(input, expected)

    def test_sample2(self):
        input = """3
1 2
1 2
1 2"""
        expected = """No"""
        self.judge(input, expected)

    def test_sample3(self):
        input = """6
-87 12
-60 -54
2 38
-76 6
87 96
-17 38"""
        expected = """Yes
-66 -57 31 -6 89 9"""
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
