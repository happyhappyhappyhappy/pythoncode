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
    N,K=MI()
    A=LI()
    # 累積和
    S=[0]*(N+1)
    # 累積和格納辞書
    nums={}
    for j in range(N):
        S[j+1]=S[j]+A[j]
    xdebug(f"S:{S}")
    for j in range(N+1):
        X=S[j]-K
        xdebug(f"{j}番目累積和 {S[j]}に対してK:{K}を引いた値X:{X}。これが以前の累積和にあるか")
        if X in nums:
            xdebug(f"X {X} は以前の累積和に登録されていた。数を足す")
            res+=nums[X]
        else:
            xdebug(f"X {X} は以前の累積和に登録されていない。パス")
        xdebug(f"{j}番目の累積和 {S[j]}を登録or加算")
        if S[j] in nums:
            nums[S[j]]+=1
        else:
            nums[S[j]]=1
    return res

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
