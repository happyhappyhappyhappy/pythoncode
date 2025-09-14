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

def right90(S):
    Supsidedown=S[::-1]
    Strans_t=list(zip(*Supsidedown))
    R=[]
    for s in Strans_t:
        R.append(list(s))
    return R

def solver():
    res=0
    N=II()
    S0=[]
    T=[]
    for _ in range(N):
        s=sys.stdin.readline().strip()
        S0.append(s)
    for _ in range(N):
        s=sys.stdin.readline().strip()
        T.append(s)
    xdebug(f"S基本={S0}")
    S1=right90(S0)
    S2=right90(S1)
    S3=right90(S2)
    diff=[0]*4
    for j in range(4):
        diff[j]=j
    for j in range(N):
        for k in range(N):
            if S0[j][k]!=T[j][k]:
                diff[0]+=1
    for j in range(N):
        for k in range(N):
            if S1[j][k]!=T[j][k]:
                diff[1]+=1
    for j in range(N):
        for k in range(N):
            if S2[j][k]!=T[j][k]:
                diff[2]+=1
    for j in range(N):
        for k in range(N):
            if S3[j][k]!=T[j][k]:
                diff[3]+=1
    res=min(diff)
    return res

def resolve():
    res=solver()
    print(res)



class TestClass(unittest.TestCase):
    def test_sample1(self):
        input = """4
###.
..#.
..#.
..#.
...#
...#
###.
...."""
        expected = """2"""
        self.judge(input, expected)

    def test_sample2(self):
        input = """13
.#..###..##..
#.#.#..#.#.#.
#.#.###..#...
###.#..#.#.#.
#.#.###..##..
.............
..#...#....#.
.##..#.#..##.
#.#..#.#.#.#.
####.#.#.####
..#..#.#...#.
..#...#....#.
.............
.............
.#....#...#..
.#...#.#..#..
####.#.#.####
.#.#.###..#.#
.##....#..##.
.#....#...#..
.............
..##..###.#.#
.#.#.#..#.###
.#.#..###.#.#
.#.#.#..#.#.#
..##..###..#."""
        expected = """5"""
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
