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

def solver():  # noqa: PLR0912
    res=[1,2,3]
    N,M=MI()
    V=[]
    for _ in range(N):
        s=input()
        V.append(s)
    xdebug(V)
    P=[0]*(N+1)
    P[0]=-1
    for j in range(M):
        zero=[]
        one=[]
        for k in range(N):
            if V[k][j]=="0":
                zero.append(k)
            else:
                one.append(k)
        xdebug(f"第{j+1}問→1 {one},0 {zero}")
        one_mem=len(one)
        zero_mem=len(zero)
        if one_mem == 0 :
            for x in zero:
                P[x+1]+=1
        elif zero_mem == 0:
            for x in one:
                P[x+1]+=1
        elif one_mem < zero_mem:
            for x in one:
                P[x+1]+=1
        else:
            for x in zero:
                P[x+1]+=1
        xdebug(f"現在のP={P}")
    max_point=max(P)
    res=[]
    for j in range(1,N+1):
        if P[j] == max_point:
            res.append(j)
    return res

def resolve():
    res=solver()
    print(*res)

class TestClass(unittest.TestCase):
    def test_sample1(self):
        input = """3 5
11100
10101
01110"""
        expected = """2 3"""
        self.judge(input, expected)

    def test_sample2(self):
        input = """5 4
0000
0000
0000
0000
0000"""
        expected = """1 2 3 4 5"""
        self.judge(input, expected)

    def test_sample3(self):
        input = """7 8
11010011
01000000
01111100
10111000
10011110
10100101
10010110"""
        expected = """1 2 3"""
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
