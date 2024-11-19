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
    res=[("|",3),("-",4),("|",2)]
    res=list()
    j=0
    N=len(S)
    while j < N:
        k=j
        ch=S[j]
        while k < N and ch == S[k]:
            k+=1
        res.append((ch,k-j))
        j=k
    return res,len(res)

def solver():
    res=0
    res=list()
    S=input().rstrip()
    RL,rllen=runlength(S)
    xdebug(f"RL={RL}")
    for j in range(rllen):
        c,cnt=RL[j]
        if c == "-":
            res.append(cnt)
    return res

def resolve():
    reslst=solver()
    print(*reslst)

class TestClass(unittest.TestCase):
    def test_sample1(self):
        input = """|---|-|----|-|-----|"""
        expected = """3 1 4 1 5"""
        self.judge(input, expected)

    def test_sample2(self):
        input = """|----------|"""
        expected = """10"""
        self.judge(input, expected)

    def test_sample3(self):
        input = """|-|-|-|------|"""
        expected = """1 1 1 6"""
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
