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

def resisDefault(res):
    for x in res :
        if x == -1:
            return True
    return False

def solver():
    res=0
    N=II()
    res=[-1]*N
    A=LI()
    r=1
    while resisDefault(res):
        # dummy
        count=0
        max_kari=-1
        for j in range(N):
            a = A[j]
            # 今順位の決まっていない物の最大値を決める
            if res[j] == -1 and max_kari <= a:
                max_kari = a
            # 今の最大値が分かる
        xdebug(f"現在の最大値は {max_kari}です")
        count=0
        for j in range(N):
            if A[j] == max_kari:
                count+=1
                res[j]=r
        r+=count
        xdebug(f"次の順位は {r} 位からです")
    return res

def resolve():
    res=solver()
    for x in res:
        print(x)

class TestClass(unittest.TestCase):
    def test_sample1(self):
        input = """4
3 12 9 9"""
        expected = """4
1
2
2"""
        self.judge(input, expected)

    def test_sample2(self):
        input = """3
3 9 6"""
        expected = """3
1
2"""
        self.judge(input, expected)

    def test_sample3(self):
        input = """4
100 100 100 100"""
        expected = """1
1
1
1"""
        self.judge(input, expected)

    def test_sample4(self):
        input = """8
87 87 87 88 41 38 41 38"""
        expected = """2
2
2
1
5
7
5
7"""
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
