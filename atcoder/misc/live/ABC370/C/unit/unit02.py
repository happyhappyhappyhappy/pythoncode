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
    S=input().rstrip()
    T=input().rstrip()
    xdebug(f"S={S},T={T}")
    res=[]
    n=len(S)
    while S!=T:
        nxt="z"*n
        for j in range(n):
            if S[j]!=T[j]:
                tmp=S[:j]+T[j]+S[j+1:]
                xdebug(f"{tmp}と{nxt}を比較")
                nxt=min(tmp,nxt)
        xdebug(f"{nxt}を回答にセット")
        res.append(nxt)
        S=nxt
    xdebug(f"最終的な値={res}")
    return res

def resolve():
    res=solver()
    print(len(res))
    for r in res:
        print(r)

class TestClass(unittest.TestCase):
    def test_sample1(self):
        input = """adbe
bcbc"""
        expected = """3
acbe
acbc
bcbc"""
        self.judge(input, expected)

    def test_sample2(self):
        input = """abcde
abcde"""
        expected = """0"""
        self.judge(input, expected)

    def test_sample3(self):
        input = """afwgebrw
oarbrenq"""
        expected = """8
aawgebrw
aargebrw
aarbebrw
aarbebnw
aarbebnq
aarbeenq
aarbrenq
oarbrenq"""
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
