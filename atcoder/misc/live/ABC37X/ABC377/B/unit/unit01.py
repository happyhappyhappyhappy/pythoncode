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
    N=8
    Field=[]
    for _ in range(N):
        Ln=input().rstrip()
        Field.append(Ln)
    xdebug(f"Field={Field}")
    Line=[1]*N
    Row=[1]*N
    # 行に存在するか求める
    for j in range(N):
        Ln=Field[j]
        if "#" in Ln:
            Line[j]=0
    # 列に存在するか求める
    xdebug(f"行の存在状況 {Line}")
    for j in range(N):
        Ln=Field[j]
        for k in range(N):
            if Ln[k] == "#":
                Row[k]=0
    xdebug(f"列の存在状況 {Row}")

    res=0
    for j in range(N):
        for k in range(N):
            if Line[j]==1 and Row[k]==1:
                xdebug(f"({j},{k})は安全ゾーン")
                res+=1
    xdebug(f"本当の回答は{res}")
    return res

def resolve():
    print(solver())

class TestClass(unittest.TestCase):
    def test_sample1(self):
        input = """...#....
#.......
.......#
....#...
.#......
........
........
..#....."""
        expected = """4"""
        self.judge(input, expected)

    def test_sample2(self):
        input = """........
........
........
........
........
........
........
........"""
        expected = """64"""
        self.judge(input, expected)

    def test_sample3(self):
        input = """.#......
..#..#..
....#...
........
..#....#
........
...#....
....#..."""
        expected = """4"""
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
