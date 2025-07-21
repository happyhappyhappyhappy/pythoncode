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
    S = []
    for _ in range(N):
        s,n=input().split()
        n=int(n)
        s=str(s)
        S.append([s,n])
    sum_leng=0
    res=""
    for _,n in S:
        sum_leng+=n
        if 100 < sum_leng:
            res="Too Long"
            return res
    for s,n in S:
        res+=s*n
    return res

def resolve():
    res=solver()
    print(res)

class TestClass(unittest.TestCase):
    def test_sample1(self):
        input = """8
m 1
i 1
s 2
i 1
s 2
i 1
p 2
i 1"""
        expected = """mississippi"""
        self.judge(input, expected)

    def test_sample2(self):
        input = """7
a 1000000000000000000
t 1000000000000000000
c 1000000000000000000
o 1000000000000000000
d 1000000000000000000
e 1000000000000000000
r 1000000000000000000"""
        expected = """Too Long"""
        self.judge(input, expected)

    def test_sample3(self):
        input = """1
a 100"""
        expected = """aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"""
        self.judge(input, expected)

    def test_sample4(self):
        input = """6
g 4
j 1
m 4
e 4
d 3
i 4"""
        expected = """ggggjmmmmeeeedddiiii"""
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
