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
    N,M=MI()
    res=[0]*M
    db=[[0]*2 for _ in range(M)]
    for _ in range(N):
        n1,g=MI()
        db[n1-1][0]+=1
        db[n1-1][1]+=g
    xdebug(db)
    for j in range(M):
        if db[j][0]!=0:
            res[j]=db[j][1]/db[j][0]
        else:
            res[j]=0.0
    xdebug(res)
    return res

def resolve():
    res=solver()
    for x in res:
        print(x)



class TestClass(unittest.TestCase):
    def test_sample1(self):
        input = """10 5
4 92
1 16
3 77
4 99
2 89
3 8
1 40
5 56
1 40
4 77"""
        expected = """32.00000000000000000000
89.00000000000000000000
42.50000000000000000000
89.33333333333333333333
56.00000000000000000000"""
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
