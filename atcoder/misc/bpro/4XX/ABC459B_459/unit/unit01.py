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

def analysys(S):
    s=S[0]
    if s in {"a", "b", "c"}:
        return "2"
    if s in {"d", "e", "f"}:
        return "3"
    if s in {"g", "h", "i"}:
        return "4"
    if s in {"j", "k", "l"}:
        return "5"
    if s in {"m", "n", "o"}:
        return "6"
    if s in {"p", "q", "r"}:
        return "7"
    if s in {"s", "t", "u"}:
        return "8"
    return "9"


def solver():
    res=0
    N=II()
    A=input().split()
    G=[]
    for j in range(N):
        x=analysys(A[j])
        G.append(x)
    res="".join(G)
    return res

def resolve():
    res=solver()
    print(res)


class TestClass(unittest.TestCase):
    def test_sample1(self):
        input = """2
algorithm heuristic"""
        expected = """24"""
        self.judge(input, expected)

    def test_sample2(self):
        input = """3
i love you"""
        expected = """459"""
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
