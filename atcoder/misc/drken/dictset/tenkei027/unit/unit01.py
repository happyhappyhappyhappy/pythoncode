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
    res=[1]
    N=II()
    S=set()
    res=[]
    for j in range(N):
        s=input().rstrip()
        if s not in S:
            res.append(j+1)
            S.add(s)
    return res,len(res)

def resolve():
    lst,cnt=solver()
    for j in range(cnt):
        print(lst[j],flush=True)

class TestClass(unittest.TestCase):
    def test_sample1(self):
        input = """5
e869120
atcoder
e869120
square1001
square1001"""
        expected = """1
2
4"""
        self.judge(input, expected)

    def test_sample2(self):
        input = """4
taro
hanako
yuka
takashi"""
        expected = """1
2
3
4"""
        self.judge(input, expected)

    def test_sample3(self):
        input = """10
square869120
square869120
square869120
square869120
square869120
square869120
square869120
square869120
square869120
square869120"""
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
