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

def dfs(N,K,R,A,res):
    if len(A)==N:
        if sum(A) % K == 0:
            res.append(A.copy())
        return
    for j in range(1,R[len(A)]+1):
        A.append(j)
        dfs(N,K,R,A,res)
        A.pop()

def solver():
    result=[[1,1,1],[2,2,2]]
    N,K=MI()
    R=LI()
    xdebug(f"N={N},K={K},R={R}")
    result=[]
    A=[]
    dfs(N,K,R,A,result)
    return result

def resolve():
    res=solver()
    for r in res:
        print(*r)

class TestClass(unittest.TestCase):
    def test_sample1(self):
        input = """3 2
2 1 3"""
        expected = """1 1 2
2 1 1
2 1 3"""
        self.judge(input, expected)

    def test_sample2(self):
        input = """1 2
1"""
        expected = """"""
        self.judge(input, expected)

    def test_sample3(self):
        input = """5 5
2 3 2 3 2"""
        expected = """1 1 1 1 1
1 2 2 3 2
1 3 1 3 2
1 3 2 2 2
1 3 2 3 1
2 1 2 3 2
2 2 1 3 2
2 2 2 2 2
2 2 2 3 1
2 3 1 2 2
2 3 1 3 1
2 3 2 1 2
2 3 2 2 1"""
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