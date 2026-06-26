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
    N=II()
    GiftL=[]
    for _ in range(N):
        line=LI()
        GiftL.append(line)
    GivenL=[[] for _ in range(N+1)]
    for j in range(N):
        line=GiftL[j]
        for k in range(1,len(line)):
            x = line[k]
            GivenL[x].append(j+1)
    res=[]
    for j in range(1,N+1):
        line=GivenL[j]
        xlen=len(line)
        outLine=[xlen,*line]
        res.append(outLine)
    return res

def resolve():
    res=solver()
    for line in res:
        print(*line)

class TestClass(unittest.TestCase):
    def test_sample1(self):
        input = """4
1 2
1 3
1 2
3 1 2 3"""
        expected = """1 4
3 1 3 4
2 2 4
0"""
        self.judge(input, expected)

    def test_sample2(self):
        input = """4
3 2 3 4
2 1 4
2 1 2
2 2 3"""
        expected = """2 2 3
3 1 3 4
2 1 4
2 1 2"""
        self.judge(input, expected)

    def test_sample3(self):
        input = """7
1 3
4 3 4 6 7
1 7
3 2 6 7
2 3 7
1 4
1 5"""
        expected = """0
1 4
3 1 2 5
2 2 6
1 7
2 2 4
4 2 3 4 5"""
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
