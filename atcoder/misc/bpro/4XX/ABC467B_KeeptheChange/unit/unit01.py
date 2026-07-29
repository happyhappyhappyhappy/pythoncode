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
    D=[]
    N=II()
    for _ in range(N):
        As,Bs,S=input().split(" ")
        # xdebug(f"{As},{Bs},{S}")
        A=int(As)
        B=int(Bs)
        F=False
        if S == "take":
            F=True
        D.append((A,B,F))
    # xdebug(D)
    # keepが有効になるケース
    X1=10000
    X2=10000
    for a,b,f in D:
        if f is True:
            X1-=a
        else:
            X1-=b
    for a,_,_ in D:
        X2-=a
    res=X2-X1
    return res

def resolve():
    res=solver()
    print(res)



class TestClass(unittest.TestCase):
    def test_sample1(self):
        input = """3
1 2 keep
3 6 take
5 9 keep"""
        expected = """5"""
        self.judge(input, expected)

    def test_sample2(self):
        input = """8
36 49 take
38 73 keep
27 85 take
65 71 take
52 86 keep
48 60 keep
37 98 keep
5 38 keep"""
        expected = """175"""
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
