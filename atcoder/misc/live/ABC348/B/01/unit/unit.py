import math
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

def dist(fromP:list,toP:list):
    fpx,fpy=fromP
    tpx,tpy=toP
    dis=math.sqrt((fpx-tpx)**2+(fpy-tpy)**2)
    return dis

def main():
    N=II()
    G=[]
    AnsList=[]
    for _ in range(N):
        x,y=MI()
        G.append([x,y])
    for j in range(N):
        maxPos=N # ダミー
        maxFar=0.0
        for k in range(N-1,-1,-1):
            if k==j:
                # xdebug(f"{k=} と {j=}は同じためジャンプします")
                continue
            else:
                dis=dist(G[j],G[k])
                if maxFar <= dis:
                    # xdebug(f"{j=} から {k=} が大きくなりました")
                    maxPos=k
                    maxFar = dis
        # xdebug(f"{j} においては 最大の位置の最小番号は{maxPos+1}です")
        AnsList.append(maxPos+1)
    ansStr="\n".join(map(str,AnsList))
    return ansStr

def resolve():
    print(main())

class TestClass(unittest.TestCase):
    def test_sample1(self):
        input = """4
0 0
2 4
5 0
3 4"""
        expected = """3
3
1
1"""
        self.judge(input, expected)

    def test_sample2(self):
        input = """6
3 2
1 6
4 5
1 3
5 5
9 8"""
        expected = """6
6
6
6
6
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