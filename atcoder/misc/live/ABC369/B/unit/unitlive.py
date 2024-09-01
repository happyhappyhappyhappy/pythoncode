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
    result=0
    N=II()
    L=[]
    R=[]
    for _ in range(N):
        V,P=input().rstrip().split(" ")
        xdebug(f"V={V},P={P}")
        if P == "L":
            L.append(int(V))
        else:
            R.append(int(V))
    xdebug(f"L={L},R={R}")
    T=0
    lenL=len(L)
    lenR=len(R)
    if lenL in (0,1):
        T=T+0
    else:
        for j in range(lenL-1):
            T=T+abs(L[j]-L[j+1])
    if lenR in (0,1):
        T=T+0
    else:
        for j in range(lenR-1):
            T=T+abs(R[j]-R[j+1])

    result=T
    return result

def resolve():
    print(solver())

class TestClass(unittest.TestCase):
    def test_sample1(self):
        input = """4
3 L
6 R
9 L
1 R"""
        expected = """11"""
        self.judge(input, expected)

    def test_sample2(self):
        input = """3
2 L
2 L
100 L"""
        expected = """98"""
        self.judge(input, expected)

    def test_sample3(self):
        input = """8
22 L
75 L
26 R
45 R
72 R
81 R
47 L
29 R"""
        expected = """188"""
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
