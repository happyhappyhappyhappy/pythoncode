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
    N=II()
    A=LI()
    nums=dict()
    for j in range(N):
        k=2
        Ai=A[j]
        xdebug(f"{Ai}の解剖開始")
        while k*k <= A[j]:
            while A[j] % (k*k) == 0:
                A[j]=A[j]//(k*k)
            k+=1
        xdebug(f"{Ai}の解剖結果 {A[j]}")
        if A[j] in nums:
            nums[A[j]]+=1
        else:
            nums[A[j]]=1
        xdebug(f"{nums}")
    if 0 in nums:
        res=(N*(N-1))//2-((N-nums[0])*(N-nums[0]-1))//2
    else:
        res=0
    for k,v in nums.items():
        if k != 0:
            res=res+(v*(v-1))//2
    return res

def resolve():
    print(solver())

class TestClass(unittest.TestCase):
    def test_sample1(self):
        input = """5
0 3 2 8 12"""
        expected = """6"""
        self.judge(input, expected)

    def test_sample2(self):
        input = """8
2 2 4 6 3 100 100 25"""
        expected = """7"""
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
