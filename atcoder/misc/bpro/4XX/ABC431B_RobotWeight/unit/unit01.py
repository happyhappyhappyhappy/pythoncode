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
    X=II()
    N=II()
    Wraw=LI()
    W=[0,*Wraw]
    box=[False]*(N+1)
    Q=II()
    now_weight=X
    res=[]
    for _ in range(Q):
        num=II()
        if box[num] is False:
            now_weight+=W[num]
            box[num]=True
        else:
            now_weight-=W[num]
            box[num]=False
        res.append(now_weight)
    return res

def resolve():
    res=solver()
    for x in res:
        print(x)

class TestClass(unittest.TestCase):
    def test_sample1(self):
        input = """31
4
15 92 65 35
4
3
1
4
1"""
        expected = """96
111
146
131"""
        self.judge(input, expected)

    def test_sample2(self):
        input = """41
10
73 8 55 26 97 48 37 47 35 55
15
1
2
7
1
6
3
10
8
4
8
1
5
9
9
3"""
        expected = """114
122
159
86
134
189
244
291
317
270
343
440
475
440
385"""
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
