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
    N=N+1
    A.append(0)
    A.sort()
    P=A.index(0)
    xdebug(f"0の位置は {P}です")
    xdebug(f"A={A}")
    L=P-1
    R=P+1
    pos=0
    xdebug(f"pos={pos}")
    for _ in range(N-1):
        xdebug(f"(L,R)=({L},{R}),pos={pos},res={res}")
        if L==-1:
            xdebug("L==-1")
            res=res+(A[R]-pos)
            pos=A[R]
            R=R+1
        elif R==N:
            xdebug(f"R=={N}")
            res=res+(pos-A[L])
            pos=A[L]
            L=L-1
        elif pos-A[L]<=A[R]-pos:
            xdebug(f"{pos}-A[{L}]<=A[{R}]-{pos}")
            res=res+(pos-A[L])
            pos=A[L]
            L=L-1
        else:
            xdebug("else")
            res=res+(A[R]-pos)
            pos=A[R]
            R=R+1
    return res

def resolve():
    res=solver()
    print(res)



class TestClass(unittest.TestCase):
    def test_sample1(self):
        input = """4
-1 -4 2 -11"""
        expected = """23"""
        self.judge(input, expected)

    def test_sample2(self):
        input = """10
1 2 3 4 5 -1 -2 -3 -4 -6"""
        expected = """17"""
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
