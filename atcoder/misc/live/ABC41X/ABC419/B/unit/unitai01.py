import os
import sys
import pprint as pp
import unittest
import heapq

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
    res=[0,0]
    Q=II()
    res=[]
    min_heap=[]
    for _ in range(Q):
        query=input().split(" ")
        q_type=int(query[0])
        if q_type == 1:
            xdebug(f"{query[1]}を箱に追加")
            value=int(query[1])
            heapq.heappush(min_heap,value)
        else:
            xdebug("最小値と取り出し")
            min_value=heapq.heappop(min_heap)
            res.append(min_value)
        xdebug(f"現在のmin_heap={min_heap}")
    return res

def resolve():
    res=solver()
    for r in res:
        print(r)

class TestClass(unittest.TestCase):
    def test_sample1(self):
        input = """5
1 6
1 7
2
1 1
2"""
        expected = """6
1"""
        self.judge(input, expected)

    def test_sample2(self):
        input = """8
1 5
1 1
1 1
1 9
2
2
1 2
2"""
        expected = """1
1
2"""
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
