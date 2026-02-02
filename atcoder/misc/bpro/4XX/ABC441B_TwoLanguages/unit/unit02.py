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
    _,_=MI()
    S=input()
    T=input()
    Q=II()
    words=[]
    for _ in range(Q):
        word=input()
        words=[*words,word]
    for word in words:
        takaFlag=True
        aoFlag=True
        for x in word:
            if x not in S:
                takaFlag=False
                break
        for x in word:
            if x not in T:
                aoFlag=False
                break
        if takaFlag is True and aoFlag is False:
            res=[*res,"Takahashi"]
        elif takaFlag is False and aoFlag is True:
            res=[*res,"Aoki"]
        else:
            res=[*res,"Unknown"]
    return res

def resolve():
    res=solver()
    for x in res:
        print(x)




class TestClass(unittest.TestCase):
    def test_sample1(self):
        input = """6 5
ahikst
aikot
5
asahi
okita
kiai
hash
it"""
        expected = """Takahashi
Aoki
Unknown
Takahashi
Unknown"""
        self.judge(input, expected)

    def test_sample2(self):
        input = """7 6
ahiknst
ahikos
5
kioki
ohiki
tashi
nishi
kashi"""
        expected = """Aoki
Aoki
Takahashi
Takahashi
Unknown"""
        self.judge(input, expected)

    def test_sample3(self):
        input = """13 11
defghiqsvwxyz
acejmoqrtwx
15
qhsqzhd
jcareec
wwqxqew
wxqxwex
jxxrtwa
trtqjxe
sqyggse
xxqwxew
xewwxxw
wwqxwex
xqqxqwq
qxxexxe
teqeroc
eeeqqee
vxdevyy"""
        expected = """Takahashi
Aoki
Unknown
Unknown
Aoki
Aoki
Takahashi
Unknown
Unknown
Unknown
Unknown
Unknown
Aoki
Unknown
Takahashi"""
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
