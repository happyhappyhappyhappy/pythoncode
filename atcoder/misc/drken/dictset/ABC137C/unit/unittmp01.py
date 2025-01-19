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
    N=II()
    D={}
    for _ in range(N):
        S=input()
        X=sorted(S)
        Xt = tuple(X)
        if Xt in D:
            D[Xt]+=1
        else:
            D[Xt]=1
    xdebug(f"{D}")
    res=0
    for v in D.values():
        x = (v * (v-1))//2
        res+=x
    xdebug(f"本当の答えは {res}")
    return res

def resolve():
    print(solver())

class TestClass(unittest.TestCase):
    def test_sample1(self):
        input = """3
acornistnt
peanutbomb
constraint"""
        expected = """1"""
        self.judge(input, expected)

    def test_sample2(self):
        input = """2
oneplustwo
ninemodsix"""
        expected = """0"""
        self.judge(input, expected)

    def test_sample3(self):
        input = """5
abaaaaaaaa
oneplustwo
aaaaaaaaba
twoplusone
aaaabaaaaa"""
        expected = """4"""
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