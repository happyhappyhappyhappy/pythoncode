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

def flugBuilt(J,K:int):
    if (J & (1<<K)) == 0:
        return False
    return True

def solver():
    res="No"
    N=7
    A=LI()
    nums={}
    cand=[]
    for j in range(1<<N):
        count=0
        for k in range(N):
            if flugBuilt(j,k):
                count +=1
        if count == 5:
            cand.append(j)
    xdebug(f"cand: {cand}")
    for j in cand:
        nums={}
        for k in range(N):
            if flugBuilt(j,k):
                card=A[k]
                if A[k] in nums:
                    nums[card]+=1
                else:
                    nums[card]=1
        newnums=sorted(nums.items(),key=lambda info:info[1])
        xdebug(f"{j}->{newnums}")
        if len(newnums) == 2:
            if newnums[0][1] == 2 and newnums[1][1]==3:
                xdebug("sucseed")
                return "Yes"
    return res

def resolve():
    print(solver())

class TestClass(unittest.TestCase):
    def test_sample1(self):
        input = """1 4 1 4 2 1 3"""
        expected = """Yes"""
        self.judge(input, expected)

    def test_sample2(self):
        input = """11 12 13 10 13 12 11"""
        expected = """No"""
        self.judge(input, expected)

    def test_sample3(self):
        input = """7 7 7 7 7 7 7"""
        expected = """No"""
        self.judge(input, expected)

    def test_sample4(self):
        input = """13 13 1 1 7 4 13"""
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
