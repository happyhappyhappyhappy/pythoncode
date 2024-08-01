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
    result=[1,1]
    H,W=MI()
    sx,sy=MI()
    C=[]
    for _ in range(H):
        Cd=list(input().split())
        C.append(Cd)
    X=input()
    xdebug(f"C={C}")
    xdebug(f"X={X}")
    sx=sx-1
    sy=sy-1
    for x in X:
        sxtmp=sx
        sytmp=sy
        if x == "U":
            xdebug("↑に進もうと思います")
            sytmp=sytmp-1
        elif x == "D":
            xdebug("↓に進もうと思います")
            sytmp=sytmp+1
        elif x == "L":
            xdebug("←に進もうと思います")
            sxtmp=sxtmp-1
        else:
            xdebug("→に進もうと思います")
            sxtmp=sxtmp+1
    return result

def resolve():
    ans=solver()
    ansstr=" ".join(map(str,ans))
    print(ansstr)

class TestClass(unittest.TestCase):
    def test_sample1(self):
        input = """2 3
2 1
.#.
...
ULDRU"""
        expected = """2 2"""
        self.judge(input, expected)

    def test_sample2(self):
        input = """4 4
4 2
....
.#..
...#
....
DUUUURULRD"""
        expected = """2 4"""
        self.judge(input, expected)

    def test_sample3(self):
        input = """6 6
1 1
.#####
######
######
######
######
######
RURLDLULLRULRDL"""
        expected = """1 1"""
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
