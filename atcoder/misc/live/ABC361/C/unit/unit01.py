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
    result = 0
    N,K=MI()
    A=LI()
    xdebug(f"A before ={A}")
    A.sort()
    xdebug(f"A after ={A}")
    result=MAXSIZE
    for j in range(K+1):
        xdebug(f"  A[{j+1}]={A[j]}をBの最小値と決め打ちます")
        xdebug(f"その上で連続する{N}-{K}の要素を残します。なお、要素A[{j+1-1}]以下は削除しています。最小値の位を取られるので")
        xdebug(f"最大値は、A[{j+(N-K)-1+1}]={A[j+(N-K)-1]}")
        minConf=A[j+(N-K)-1]-A[j]
        xdebug(f"{result}と{minConf}を比較します")
        if minConf < result:
            xdebug(f"今回の{minConf}の方が小さい->Change")
            result=minConf
        else:
            xdebug(f"{result}の方がまだ大きい。そのまま")
    return result

def resolve():
    print(solver())

class TestClass(unittest.TestCase):
    def test_sample1(self):
        input = """5 2
3 1 5 4 9"""
        expected = """2"""
        self.judge(input, expected)

    def test_sample2(self):
        input = """6 5
1 1 1 1 1 1"""
        expected = """0"""
        self.judge(input, expected)

    def test_sample3(self):
        input = """8 3
31 43 26 6 18 36 22 13"""
        expected = """18"""
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
