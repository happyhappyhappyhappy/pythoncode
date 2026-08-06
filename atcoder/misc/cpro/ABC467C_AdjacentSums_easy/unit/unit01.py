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
    res=200001
    N,M=MI()
    A=LI()
    B=LI()
    A1=A.copy()
    A2=A.copy()
    # Aの最後に手を付けないケース
    res1=0
    for j in range(N-1,0,-1):
        if (A1[j]+A1[j-1])%M!=B[j-1]:
            res1+=1
            A1[j-1]+=1
    res=min(res1,res)
    # Aの最後に手を付けるケース
    res2=0
    A2[N-1]+=1
    for j in range(N-1,0,-1):
        if(A2[j]+A2[j-1]%M)!=B[j-1]:
            res2+=1
            A2[j-1]+=1
    res=min(res,res2)
    return res

def resolve():
    res=solver()
    print(res)



class TestClass(unittest.TestCase):
    def test_sample1(self):
        input = """3 2
1 1 1
1 1"""
        expected = """1"""
        self.judge(input, expected)

    def test_sample2(self):
        input = """2 2
1 1
0"""
        expected = """0"""
        self.judge(input, expected)

    def test_sample3(self):
        input = """10 2
0 0 0 1 1 0 1 0 1 0
0 1 0 1 0 1 0 1 0"""
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
