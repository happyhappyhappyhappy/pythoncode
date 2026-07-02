import bisect
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
    N=II()
    H_List=[]
    L_List=[]
    for _ in range(N):
        H,L=MI()
        H_List.append(H)
        L_List.append(L)
    max_list=[]
    nowmax=0
    for j in range(N-1,-1,-1):
        nowmax=max(nowmax,H_List[j])
        max_list.append(nowmax)
    max_list.reverse()
    xdebug(f"現在の高さリスト {max_list}")
    xdebug(f"去る時間リスト   {L_List}")
    _=II()
    Q=LI()
    for q in Q:
        index=bisect.bisect_right(L_List,q)
        xdebug(f"{q}+0.5は {index}に所属します")
        res.append(max_list[index])
    return res

def resolve():
    res=solver()
    for r in res:
        print(r)



class TestClass(unittest.TestCase):
    def test_sample1(self):
        input = """4
31 4
26 5
3 5
15 9
4
3 4 5 6"""
        expected = """31
26
15
15"""
        self.judge(input, expected)

    def test_sample2(self):
        input = """10
587 138
772 155
755 404
519 408
529 432
169 586
114 632
249 656
329 972
299 984
14
443 801 824 276 399 314 300 510 311 580 498 930 359 5"""
        expected = """329
329
329
755
755
755
755
329
755
329
329
329
755
772"""
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
