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
    result=["sample","test"]
    N=II()
    S=[]
    for _ in range(N):
        Sdec=input()
        S.append(Sdec)
    xdebug(f"S={S}")
    for j in range(N):
        Sdec=S[j]
        Sdeclen=len(Sdec)
        for k in range(Sdeclen):
            xdebug(f"Sの {j} 番目 {k} 個目の値は {Sdec[k]} です")
    M=0
    for j in range(N):
        M=max(len(S[j]),M)
    xdebug(f"M={M}")
    T=[["*"] * N for _ in range(M)]
    xdebug(f"T={T}")
    result=[]
    for j in range(M):
        Tdec=T[j]
        Tdecstr="".join(Tdec)
        result.append(Tdecstr)
    return result

def resolve():
    result=solver()
    resstr="\n".join(result)
    print(resstr)

class TestClass(unittest.TestCase):
    def test_sample1(self):
        input = """3
abc
de
fghi"""
        expected = """fda
geb
h*c
i"""
        self.judge(input, expected)

    def test_sample2(self):
        input = """3
atcoder
beginner
contest"""
        expected = """cba
oet
ngc
tio
end
sne
ter
*r"""
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
