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
    res=[]
    N=II()
    S=input()
    ans=0
    k=0
    for j in range(N):
        xdebug(f"----No.{j}----")
        if S[j]=="x":
            xdebug(f"{j}はxですストップします")
            k+=1
            xdebug(f"k={k}になりました")
            ans+=1
            xdebug(f"ans={ans}になりました。これは出力対象です。")
            res.append(ans)
        else:
            ans+=1
            xdebug(f"ans={ans}になりました。これは出力対象になりません。")
    if k < N:
        xdebug(f"kが {k} で N {N}に至っていないので全部取った")
        for _ in range(N-k):
            xdebug(f"{N}追加")
            res=[*res,N]
    return res

def resolve():
    res=solver()
    for x in res:
        print(x)



class TestClass(unittest.TestCase):
    def test_sample1(self):
        input = """5
oxoxo"""
        expected = """2
4
5
5
5"""
        self.judge(input, expected)

    def test_sample2(self):
        input = """3
ooo"""
        expected = """3
3
3"""
        self.judge(input, expected)

    def test_sample3(self):
        input = """1
x"""
        expected = """1"""
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
