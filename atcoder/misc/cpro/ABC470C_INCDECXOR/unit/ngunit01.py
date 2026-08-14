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
    res=[]
    N,Q=MI()
    A=[0]*N
    for _ in range(Q):
        q=input().split()
        if q[0] == "1":
            xdebug("Queue--1")
            pos=int(q[1])-1
            A[pos]+=1
            XOR=A[0]
            xdebug(f"0 -> {XOR:b}")
            for j in range(1,N):
                XOR=XOR^A[j]
                xdebug(f"{j} -> {XOR:b}")
            res.extend([XOR])
        else:
            xdebug("Queue--2")
            for j in range(N):
                if 1 <= A[j]:
                    A[j]-=1
            XOR=A[0]
            xdebug(f"0 -> {XOR:b}")
            for j in range(1,N):
                XOR=XOR^A[j]
                xdebug(f"{j} -> {XOR:b}")
            res.extend([XOR])
    return res

def resolve():
    res=solver()
    for x in res:
        print(x)


class TestClass(unittest.TestCase):
    def test_sample1(self):
        input = """2 5
1 2
1 2
1 1
2
2"""
        expected = """1
2
3
1
0"""
        self.judge(input, expected)

    def test_sample2(self):
        input = """3 8
1 2
1 3
1 1
1 2
1 1
2
1 3
1 1"""
        expected = """1
0
1
2
1
0
1
2"""
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
