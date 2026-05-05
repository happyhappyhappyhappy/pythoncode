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
    H,W=MI()
    G=[]
    for _ in range(H):
        line=input()
        G.append(line)
    xdebug(G)
    for h1 in range(H):
        for h2 in range(h1+1,H+1):
            for w1 in range(W):
                for w2 in range(w1+1,W+1):
                    flag=True
                    for j in range(h1,h2):
                        for k in range(w1,w2):
                            jm = h1+h2-1-j
                            km = w1+w2-1-k
                            if G[j][k] != G[jm][km]:
                                flag=False
                    if flag is True:
                        xdebug(f"縦[{h1},{h2}]横[{w1},{w2}]は点対称になります")
                        res+=1

    return res

def resolve():
    res=solver()
    print(res)



class TestClass(unittest.TestCase):
    def test_sample1(self):
        input = """3 2
.#
#.
##"""
        expected = """10"""
        self.judge(input, expected)

    def test_sample2(self):
        input = """4 5
.#.#.
####.
##..#
....#"""
        expected = """54"""
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
