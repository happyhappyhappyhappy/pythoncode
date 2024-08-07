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

def solver(N:int,A:int,B:int,D:list):
    Week=A+B
    Pos=set()
    for j in range(N):
        x=D[j]%Week
        Pos.add(x)
    if len(Pos) == 1:
        return "Yes"
    SL=list(Pos)
    SL.sort()
    # SLstr=" ".join(map(str,SL))
    # xdebug(f"{SLstr=}")
    SN=len(SL)
    flg=False
    for j in range(SN-1):
        x = (SL[j+1]-SL[j])%Week
        if x > B:
            flg=True
            return "Yes"
    if flg is False:
        x = (SL[0]-SL[SN-1])%Week
        if x > B:
            return "Yes"
    return "No"

def main():
    N,A,B=MI()
    D=LI()
    return solver(N,A,B,D)

def resolve():
    print(f"{main()}")

class TestClass(unittest.TestCase):
    def test_sample1(self):
        input = """3 2 5
1 2 9"""
        expected = """Yes"""
        self.judge(input, expected)

    def test_sample2(self):
        input = """2 5 10
10 15"""
        expected = """No"""
        self.judge(input, expected)

    def test_sample3(self):
        input = """4 347 347
347 700 705 710"""
        expected = """Yes"""
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
