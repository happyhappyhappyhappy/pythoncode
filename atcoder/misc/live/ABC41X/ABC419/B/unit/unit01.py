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
    res=[0,0]
    Q=II()
    B=[]
    res=[]
    for _ in range(Q):
        S=input()
        if S[0]=="1":
            x,ystr=S.split(" ")
            y=int(ystr)
            xdebug(f"{y}を入れます")
            B.append(y)
        else:
            xdebug("最小を求めます")
            min_a=min(B)
            res.append(min_a)
            B.remove(min_a)
    return res

def resolve():
    res=solver()
    for a in res:
        print(a)

class TestClass(unittest.TestCase):
    def test_sample1(self):
        input = """5
1 6
1 7
2
1 1
2"""
        expected = """6
1"""
        self.judge(input, expected)

    def test_sample2(self):
        input = """8
1 5
1 1
1 1
1 9
2
2
1 2
2"""
        expected = """1
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
