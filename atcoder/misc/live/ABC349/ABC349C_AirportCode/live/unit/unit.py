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

def solver():
    S=SI()
    T=SI()
    S2=S.upper()
    s_pos=0
    t_pos=0
    flg=False
    while s_pos < len(S2):
        if S2[s_pos] == T[t_pos]:
            t_pos=t_pos+1
            if t_pos==3:
                flg=True
                break
        s_pos=s_pos+1
    # 敗者復活戦
    if t_pos == 2 and T[2]=="X":
        flg=True
    if flg is True:
        return "Yes"
    else:
        return "No"

def resolve():
    print(solver())

class TestClass(unittest.TestCase):
    def test_sample1(self):
        input = """narita
NRT"""
        expected = """Yes"""
        self.judge(input, expected)

    def test_sample2(self):
        input = """losangeles
LAX"""
        expected = """Yes"""
        self.judge(input, expected)

    def test_sample3(self):
        input = """snuke
RNG"""
        expected = """No"""
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
