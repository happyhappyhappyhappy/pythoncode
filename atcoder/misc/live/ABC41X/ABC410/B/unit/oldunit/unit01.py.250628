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
    res=[1,2,3,4,5]
    N,Q=MI()
    QList=LI()
    xdebug(f"N={N},Q={Q}")
    xdebug(f"QList={QList}")
    BOX=[0]*(N+1)
    res=[]
    BOX[0]=MAXSIZE
    for x in QList:
        if x == 0:
            minball=min(BOX)
            for j in range(1,N+1):
                if minball == BOX[j]:
                    BOX[j]+=1
                    res.append(j)
                    break
        else :
            BOX[x]+=1
            res.append(x)
    return res

def resolve():
    res=solver()
    print(*res)

class TestClass(unittest.TestCase):
    def test_sample1(self):
        input = """4 5
2 0 3 0 0"""
        expected = """2 1 3 4 1"""
        self.judge(input, expected)

    def test_sample2(self):
        input = """3 7
1 1 0 0 0 0 0"""
        expected = """1 1 2 3 2 3 1"""
        self.judge(input, expected)

    def test_sample3(self):
        input = """6 20
4 6 0 3 4 2 6 5 2 3 0 3 2 5 0 3 5 0 2 0"""
        expected = """4 6 1 3 4 2 6 5 2 3 1 3 2 5 1 3 5 4 2 6"""
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
