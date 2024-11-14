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
# d : 提出日
# q : 回収周期
# r : 余り
def algofunc(d,q,r):
    res=0
    dr=d-r
    kr=(dr+q-1)//q
    r0=kr*q
    res=r0+r
    xdebug(f"まず 出された日から余り{r}を引きます {dr}")
    xdebug(f"これを 周期{q}で割ったときの切り上げを求めます {kr}")
    xdebug(f"ここよりもし 余りなければ {r0}に回収です")
    xdebug(f"これにあまりを加えると {res}になります")
    return res

def solver():
    res2=0
    N=II()
    qr = list()
    pd = list()
    for _ in range(N):
        q,r=MI()
        qr.append((q,r))
    Q=II()
    res=list()
    for _ in range(Q):
        pat,d=MI()
        q,r=qr[pat-1]
        x=algofunc(d,q,r)
        res.append(x)
    return res

def resolve():
    reslist=solver()
    reslen=len(reslist)
    for j in range(reslen):
        print(reslist[j])

class TestClass(unittest.TestCase):
    def test_sample1(self):
        input = """2
7 3
4 2
5
1 1
1 3
1 4
1 15
2 7"""
        expected = """3
3
10
17
10"""
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
