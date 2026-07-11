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
    res=[]
    N,M=MI()
    D=[[] for _ in range(M+1)]
    colors=[0]*(N+1)
    kinds=0
    for _ in range(N):
        a,d,b=MI()
        D[d].append((a,b))
        if colors[a]==0:
            kinds+=1
        colors[a]+=1
    for j in range(1,M+1):
        column=D[j]
        for a,b in column:
            if colors[a]==0:
                kinds+=1
            colors[a]+=1
            colors[b]-=1
            if colors[b]==0:
                kinds-=1
        res.append(kinds)
    return res

def resolve():
    res=solver()
    for r in res:
        print(r)



class TestClass(unittest.TestCase):
    def test_sample1(self):
        input = """6 7
1 3 2
2 6 5
5 5 1
3 3 5
4 1 6
6 3 6"""
        expected = """5
5
3
3
4
4
4"""
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
