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
    A=[]
    for _ in range(3):
        column=LI()
        A.append(column)
    xdebug(A)
    count=0
    for x in range(6):
        for y in range(6):
            for z in range(6):
               Ax=A[0][x]
               By=A[1][y]
               Cz=A[2][z]
               T=[Ax,By,Cz]
               T.sort()
               if T == [4,5,6]:
                   xdebug(f"サイコロの目は {Ax} {By} {Cz}です")
                   count+=1
    value=count/(6*6*6)
    res=f"{value:.10f}"
    return res

def resolve():
    res=solver()
    print(res)



class TestClass(unittest.TestCase):
    def test_sample1(self):
        input = """1 2 3 4 5 6
1 2 3 4 5 6
1 2 3 4 5 6"""
        expected = """0.0277777778"""
        self.judge(input, expected)

    def test_sample2(self):
        input = """4 5 6 4 5 6
4 4 5 5 6 6
6 5 4 4 5 6"""
        expected = """0.2222222222"""
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
