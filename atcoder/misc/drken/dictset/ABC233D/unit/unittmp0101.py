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
    res2=0
    N,K=MI()
    A=LI()
    S=[0]*(N+1)
    for j in range(N):
        S[j+1]=S[j]+A[j]
    print(*S)
    nums=dict()
    res=0
    for j in range(N+1):
        D=S[j]-K
        xdebug(f"S[{j}]={S[j]}に置ける D={D}")
        if D in nums:
            xdebug(f"{D}におけるnumsの値を回答に追加")
            res=res+nums[D]
        if S[j] in nums:
            nums[S[j]]+=1
        else:
            nums[S[j]]=1
        xdebug(f"j={j} に置ける num={nums}")
    xdebug(f"本当の答えは {res}")
    return res2

def resolve():
    print(solver())

class TestClass(unittest.TestCase):
    def test_sample1(self):
        input = """6 5
8 -3 5 7 0 -4"""
        expected = """3"""
        self.judge(input, expected)

    def test_sample2(self):
        input = """2 -1000000000000000
1000000000 -1000000000"""
        expected = """0"""
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
