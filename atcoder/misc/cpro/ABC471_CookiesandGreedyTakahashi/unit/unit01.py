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
    N+=1
    A=LI()
    A.append(0)
    A.sort()
    P=A.index(0)
    L=P-1
    R=P+1
    pos=0
    for j in range(N-1):
        xdebug(f"---- Term {j} ----")
        if L == -1:
            xdebug(f"左隅です {pos}->{A[R]}へ移動")
            res+=(A[R]-pos)
            pos=A[R]
            R+=1
        elif R == N:
            xdebug(f"右隅です {pos}->{A[L]}へ移動")
            res+=(pos-A[L])
            pos=A[L]
            L-=1
        else:
            xdebug("中間です")
            LEFT=pos-A[L]
            RIGHT=A[R]-pos
            if LEFT <= RIGHT:
                xdebug(f"左側の距離が近いので {pos}->{A[L]}へ移動")
                res+=LEFT
                pos=A[L]
                L-=1
            else:
                xdebug(f"右側の距離が近いので {pos}->{A[R]}へ移動")
                res+=RIGHT
                pos=A[R]
                R+=1
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
