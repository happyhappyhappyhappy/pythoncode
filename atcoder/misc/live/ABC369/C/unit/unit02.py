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
def SI(): return sys.stdin.readline().strip()
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
    N=II()
    res=N
    A=LI()
    n=len(A)
    B=[]
    for j in range(n-1):
        x=A[j+1]-A[j]
        B.append(x)
    xdebug(f"B={B}")
    SM=[]
    key=0
    m=len(B)
    while key < m:
        num=B[key]
        k=key
        while k < m and B[k]==B[key]:
            k+=1
        leng=k-key
        SM.append((num,leng))
        key=k
    xdebug(f"SM={SM}")
    for s,m in SM:
        xdebug(f"{s}の個数{m}")
        x=((m+1)*m)//2
        xdebug(f"{x}通りある")
        res+=((m+1)*m)//2
    return res

def resolve():
    print(solver())

class TestClass(unittest.TestCase):
    def test_sample1(self):
        input = """4
3 6 9 3"""
        expected = """8"""
        self.judge(input, expected)

    def test_sample2(self):
        input = """5
1 1 1 1 1"""
        expected = """15"""
        self.judge(input, expected)

    def test_sample3(self):
        input = """8
87 42 64 86 72 58 44 30"""
        expected = """22"""
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
