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
    ans="No"
    WL=list(sys.stdin.readline().rstrip().split())
    xdebug(f"WL={WL}")
    S=WL[0]
    T=WL[1]
    for j in range(1,len(S)):
        xdebug(f"(1) {S} から {j}個ずつ切り出す")
        for k in range(j):
            xdebug(f"  (2) {j}個の物から{k+1}番目を選択")
            x=""
            for m in range(k,len(S),j):
                xdebug(f"    (3) {m+1}番目を文字列結合")
                x=x+S[m]
                xdebug(f"    結果 {x}")
            xdebug(f"最終結果 {x}")
    return ans

def resolve():
    print(solver())

class TestClass(unittest.TestCase):
    def test_sample1(self):
        input = """atcoder toe"""
        expected = """Yes"""
        self.judge(input, expected)

    def test_sample2(self):
        input = """beginner r"""
        expected = """No"""
        self.judge(input, expected)

    def test_sample3(self):
        input = """verticalreading agh"""
        expected = """No"""
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
