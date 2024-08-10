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
    result="infinite"
    N,M=MI()
    A=LI()
    total=0
    for j in range(N):
        total=total+A[j]
    if total <= M:
        return result
    result=0
    ans=0
    ok=0
    ng=MAXSIZE
    while 1 < abs(ng-ok):
        mid=(ok+ng)//2
        subtotal=0
        for j in range(N):
            subtotal=subtotal+min(mid,A[j])
        if subtotal <= M:
            xdebug(f"{mid}でOK")
            ok = mid
        else:
            xdebug(f"{mid}ではNG")
            ng = mid
        if 1 < abs(ng-ok):
            xdebug("さらに探求")
    result=ok
    return result

def resolve():
    print(solver())

class TestClass(unittest.TestCase):
    def test_sample1(self):
        input = """4 8
1 3 2 4"""
        expected = """2"""
        self.judge(input, expected)

    def test_sample2(self):
        input = """3 20
5 3 2"""
        expected = """infinite"""
        self.judge(input, expected)

    def test_sample3(self):
        input = """10 23
2 5 6 5 2 1 7 9 7 2"""
        expected = """2"""
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
