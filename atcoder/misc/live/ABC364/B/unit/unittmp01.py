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
    result=[0,0]
    H,W=MI()
    Si,Sj=MI()
    xdebug(f"H={H},W={W},Si={Si},Sj={Sj}")
    C=[]
    for _ in range(H):
        Cp=input()
        C.append(Cp)
    X=input()
    Si=Si-1
    Sj=Sj-1
    for x in range(len(X)):
        d=X[x]
        if d == "U":
            xdebug("次は↑に移動します")
            Sit=Si-1
            Sjt=Sj
            xdebug(f"移動箇所は x = {Sjt+1},y = {Sit+1}です")
            if 0 < Sit and C[Sit][Sjt] != "#":
                Si = Sit
                Sj = Sjt
                xdebug("問題ないので移動します")
        elif d == "D":
            xdebug("次は↓に移動します")
            Sit=Si+1
            Sjt=Sj
            xdebug(f"移動箇所は x = {Sjt+1},y = {Sit+1}です")
            if Sit < H and C[Sit][Sjt] != "#":
                Si = Sit
                Sj = Sjt
                xdebug("問題ないので移動します")
        elif d == "L":
            xdebug("次は←に移動します")
            Sit=Si
            Sjt=Sj-1
            xdebug(f"移動箇所は x = {Sjt+1},y = {Sit+1}です")
            if 0 < Sjt  and C[Sit][Sjt] != "#":
                Si = Sit
                Sj = Sjt
                xdebug("問題ないので移動します")
        else :
            xdebug("次は→に移動します")
            Sit=Si
            Sjt=Sj+1
            xdebug(f"移動箇所は x = {Sjt+1},y = {Sit+1}です")
            if Sjt < W  and C[Sit][Sjt] != "#":
                Si = Sit
                Sj = Sjt
                xdebug("問題ないので移動します")
    result=[Si+1,Sj+1]
    return result

def resolve():
    result=solver()
    pres=" ".join(map(str,result))
    print(pres)

class TestClass(unittest.TestCase):
    def test_sample1(self):
        input = """2 3
2 1
.#.
...
ULDRU"""
        expected = """2 2"""
        self.judge(input, expected)

    def test_sample2(self):
        input = """4 4
4 2
....
.#..
...#
....
DUUUURULRD"""
        expected = """2 4"""
        self.judge(input, expected)

    def test_sample3(self):
        input = """6 6
1 1
.#####
######
######
######
######
######
RURLDLULLRULRDL"""
        expected = """1 1"""
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
