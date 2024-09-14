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

def trans(s):
    return (int(s[0]),s[1])

def solver():
    N,M=MI()
    Flugs=[False]*(N+1)
    res=[]
    for _ in range(M):
        L=input().rstrip().split()

        no,form=trans(L)
        xdebug(f"{no}番で{form}が生まれた")
        if Flugs[no] is False and form=="M":
            res.append("Yes")
            Flugs[no]=True
        elif Flugs[no] is True and form=="M":
            res.append("No")
        else:
            res.append("No")
    return res

def resolve():
    res=solver()
    for r in res:
        print(r)

class TestClass(unittest.TestCase):
    def test_sample1(self):
        input = """2 4
1 M
1 M
2 F
2 M"""
        expected = """Yes
No
No
Yes"""
        self.judge(input, expected)

    def test_sample2(self):
        input = """4 7
2 M
3 M
1 F
4 F
4 F
1 F
2 M"""
        expected = """Yes
Yes
No
No
No
No
No"""
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
