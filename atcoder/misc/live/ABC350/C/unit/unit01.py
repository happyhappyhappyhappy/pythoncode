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
    N=II()
    A=LI()
    W=[0]*N
    AL=[]
    for j in range(N):
        A[j]=A[j]-1
        W[A[j]]=j
    for j in range(N-1):
        if A[j]==j:
            continue
        k=W[j]
        t=W[A[j]]
        W[A[j]]=W[A[k]]
        W[A[k]]=t
        t=A[j]
        A[j]=A[k]
        A[k]=t
        AL.append([j,k])
    lg=len(AL)
    print(lg)
    for j in range(lg):
        a,b=AL[j]
        print(f"{a+1} {b+1}")


def resolve():
    # print(solver())
    solver()

class TestClass(unittest.TestCase):
    def test_sample1(self):
        input = """5
3 4 1 2 5"""
        expected = """2
1 3
2 4"""
        self.judge(input, expected)

    def test_sample2(self):
        input = """4
1 2 3 4"""
        expected = """0"""
        self.judge(input, expected)

    def test_sample3(self):
        input = """3
3 1 2"""
        expected = """2
1 2
2 3"""
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
