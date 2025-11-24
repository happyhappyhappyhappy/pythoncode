import os
import sys
import pprint as pp
import unittest

from collections import Counter
from io import StringIO
from typing import List,Dict
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

def splitsubstr(N,K,S)->List:
    res=[]
    for j in range(N-K+1):
        subS=S[j:j+K]
        res.append(subS)
    return res

def solver():
    N,K=MI()
    S=input().rstrip()
    subS=splitsubstr(N,K,S)
    count=Counter(subS)
    maxcnt=max(count.values())
    res=[]
    for substring,value in count.items():
        if value == maxcnt:
            res.append(substring)
    return maxcnt,res

def resolve():
    k,res=solver()
    print(k)
    print(*res)



class TestClass(unittest.TestCase):
    def test_sample1(self):
        input = """9 3
ovowowovo"""
        expected = """2
ovo owo"""
        self.judge(input, expected)

    def test_sample2(self):
        input = """9 1
ovowowovo"""
        expected = """5
o"""
        self.judge(input, expected)

    def test_sample3(self):
        input = """35 3
thequickbrownfoxjumpsoverthelazydog"""
        expected = """2
the"""
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
