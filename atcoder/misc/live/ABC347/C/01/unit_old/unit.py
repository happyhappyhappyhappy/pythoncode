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

def hList(S:list,D:int):
    dSet=set()
    for j in range(len(S)):
        x = S[j] % D
        dSet.add(x)
    xdebug(f"ぎゅっとまとめたら->{dSet}")
    ansList=list(sorted(dSet))
    # xdebug(f"さらにソート{ansList}")
    return ansList

def check(L:list,A:int,B:int):
    N=len(L)
    if N == 1:
        return "Yes"
    for j in range(N-1):
        d1=L[j]
        pos=(j+1)%(N)
        d2=L[pos]
        if (d2-d1)%(A+B) > B:
            return "Yes"
    return "No"

def solver(N:int,A:int,B:int,S:list):
    xdebug(f"{N=},{A=},{B=}")
    xdebug(f"LIST={S}")
    GList=hList(S,A+B)
    xdebug(f"{GList=}")
    ans = check(GList,A,B)
    return ans

def resolve():
    N,A,B=MI()
    S=LI()
    print(f"{solver(N,A,B,S)}")

class TestClass(unittest.TestCase):
    def test_sample1(self):
        input = """3 2 5
1 2 9"""
        expected = """Yes"""
        self.judge(input, expected)

    def test_sample2(self):
        input = """2 5 10
10 15"""
        expected = """No"""
        self.judge(input, expected)

    def test_sample3(self):
        input = """4 347 347
347 700 705 710"""
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
