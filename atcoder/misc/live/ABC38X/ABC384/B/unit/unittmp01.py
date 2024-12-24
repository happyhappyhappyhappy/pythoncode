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
    N,R=MI()
    for j in range(N):
        xdebug(f"{j+1}回目 現在のレート {R}")
        Div, A = MI()
        if Div == 1 :
            if  1600 <= R and R <= 2799:
                xdebug(f"{j+1}回目 予定通り Div1のテストに参加します")
                R+=A
            else:
                xdebug(f"{j+1}回目 参加資格がないのでDiv1には参加できません")
        if Div == 2:
            if 1200 <= R and R <= 2399:
                xdebug(f"{j+1}回目 予定通りDiv2テストに参加します")
                R+=A
            else:
                xdebug(f"{j+1}回目 資格がないのでDiv2テストに参加できません")
    xdebug(f"最終レート {R}")
    return R

def resolve():
    print(solver())

class TestClass(unittest.TestCase):
    def test_sample1(self):
        input = """4 1255
2 900
1 521
2 600
1 52"""
        expected = """2728"""
        self.judge(input, expected)

    def test_sample2(self):
        input = """2 3031
1 1000
2 -1000"""
        expected = """3031"""
        self.judge(input, expected)

    def test_sample3(self):
        input = """15 2352
2 -889
2 420
2 -275
1 957
1 -411
1 -363
1 151
2 -193
2 289
2 -770
2 109
1 345
2 551
1 -702
1 355"""
        expected = """1226"""
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
