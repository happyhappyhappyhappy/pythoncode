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

def runlength(S):
    N=len(S)
    res=list()
    j=0
    while j < N:
        c=S[j]
        k=j
        while  k < N and S[k]==c:
            k+=1
        nlen=k-j
        res.append((c,nlen))
        j=k
    return res

def solver():
    res=0
    N,K=MI()
    S=input().rstrip()
    xdebug(f"S={S}")
    RL=runlength(S)
    xdebug(f"RL={RL}")
    rllist=len(RL)
    for j in range(rllist):
        c,cnt=RL[j]
        if c=="O":
            x=cnt//K
            res+=x

    return res

def resolve():
    print(solver())

class TestClass(unittest.TestCase):
    def test_sample1(self):
        input = """7 3
OOXOOOO"""
        expected = """1"""
        self.judge(input, expected)

    def test_sample2(self):
        input = """12 2
OXXOOOXOOOOX"""
        expected = """3"""
        self.judge(input, expected)

    def test_sample3(self):
        input = """22 5
XXOOOOOOOOXXOOOOOXXXXX"""
        expected = """2"""
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
