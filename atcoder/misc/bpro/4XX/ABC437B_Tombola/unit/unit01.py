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
    res=0
    H,_,N=MI()
    G=[]
    Ball=[]
    for _ in range(H):
        grid=LI()
        G=[*G,grid]
    for _ in range(N):
        b=II()
        Ball=[*Ball,b]
#    xdebug(f"{G}")
#    xdebug(f"{Ball}")
    for j in range(H):
        nowB=0
        line=G[j]
        for b in Ball:
            if b in line:
                nowB+=1
        res=max(res,nowB)

    return res

def resolve():
    res=solver()
    print(res)



class TestClass(unittest.TestCase):
    def test_sample1(self):
        input = """3 4 5
12 3 5 7
6 10 11 9
1 2 4 8
2
4
9
6
11"""
        expected = """3"""
        self.judge(input, expected)

    def test_sample2(self):
        input = """3 5 2
81 63 31 16 15
30 3 6 54 24
26 41 48 64 66
44
79"""
        expected = """0"""
        self.judge(input, expected)

    def test_sample3(self):
        input = """3 5 12
78 19 70 58 83
12 30 80 20 27
48 71 8 43 82
82
30
43
8
80
70
20
78
12
71
19
48"""
        expected = """5"""
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
