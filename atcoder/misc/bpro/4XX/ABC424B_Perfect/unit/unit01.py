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
    N,M,K=MI()
    Table=[[False for _ in range(M)] for _ in range(N)]
    xdebug(Table)
    AllOK=[False for _ in range(N)]
    for _ in range(K):
        Per,Pro=MI()
        Table[Per-1][Pro-1]=True
        for j in range(N):
            isOK=True
            for k in range(M):
                if Table[j][k] is False:
                    isOK=False
                    break
            if isOK is True and AllOK[j] is False:
                xdebug(f"{j+1} 番が問題を全て正解しました")
                res.append(j+1)
                AllOK[j]=True
    xdebug(Table)
    return res

def resolve():
    res=solver()
    print(*res)



class TestClass(unittest.TestCase):
    def test_sample1(self):
        input = """3 2 5
1 1
3 2
2 1
3 1
1 2"""
        expected = """3 1"""
        self.judge(input, expected)

    def test_sample2(self):
        input = """2 2 2
1 1
2 2"""
        expected = """"""
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
