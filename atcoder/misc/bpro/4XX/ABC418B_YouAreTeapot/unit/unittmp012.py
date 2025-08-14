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
    res=0.0
    S=input()
    N=len(S)
    for j in range(N):
        if S[j] != "t":
            continue
        for k in range(j+2,N):
            if S[k] != "t":
                continue
            sub=S[j:k+1]
            xdebug(f"{j}->{k}=[{sub}]->長さ {len(sub)}")
            cnt=sub.count("t")
            Nsub=len(sub)
            fle=(cnt-2)/(Nsub-2)
            res=max(res,fle)
    return res

def resolve():
    res=solver()
    print(res)

class TestClass(unittest.TestCase):
    def test_sample1(self):
        input = """attitude"""
        expected = """0.50000000000000000"""
        self.judge(input, expected)

    def test_sample2(self):
        input = """ottottott"""
        expected = """0.66666666666666667"""
        self.judge(input, expected)

    def test_sample3(self):
        input = """coffeecup"""
        expected = """0.00000000000000000"""
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
