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

def isOK(T,M,A):
    result=False
    xdebug(f"検査 {T}")
    targetCheck=0
    for a in A:
        targetCheck+=min(a,T)
    if targetCheck <= M:
        xdebug(f"検査結果 {targetCheck} <= 可能値 {M}->OK")
        result=True
    else:
        xdebug(f"可能値  {M} < 検査結果 {targetCheck} ->NG")

    return result

def m_bisect(M,A):
    ok=0
    ng=MAXSIZE
    while 1 < abs(ng-ok):
        mid=(ng+ok)//2
        if isOK(mid,M,A):
            xdebug(f"チェック値 {mid}は OK これをOK値に入れて↑を考える")
            ok=mid
        else:
            xdebug(f"チェック値 {mid}は ng これをng値に入れて↓を考える")
            ng=mid
    xdebug(f"ok {ok} < ng {ng} と差が1になりました 終わり")
    return ok

def solver():
    result="infinite"
    N,M=MI()
    A=LI()
    sumA=sum(A)
    if sumA <= M:
        xdebug(f"合計 {sumA} <= 最大可能量 {M}なので無限に出来ます")
        return result
    else:
        result=0
    result=m_bisect(M,A)
    return result

def resolve():
    print(solver())

class TestClass(unittest.TestCase):
    def test_sample1(self):
        input = """4 8
1 3 2 4"""
        expected = """2"""
        self.judge(input, expected)

    def test_sample2(self):
        input = """3 20
5 3 2"""
        expected = """infinite"""
        self.judge(input, expected)

    def test_sample3(self):
        input = """10 23
2 5 6 5 2 1 7 9 7 2"""
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
