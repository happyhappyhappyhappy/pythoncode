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
N=300000
M=300000

def solver():
    res=0
    m=0
    idx=0
    r=[0]*(M+1)
    c=[0]*(M+1)
    rowPlace=[0]*(N+1)
    columnPlace=[0]*(N+1)
    _,m=MI()
    for j in range(1,m+1):
        r[j],c[j]=MI()
        rp=rowPlace[r[j]]
        cp=columnPlace[c[j]]
        xdebug(f"-----No {j}-----")
        xdebug(f"({r[j]},{c[j]})=>({rp},{cp})")
        if 0 < rowPlace[r[j]]:
            idx=rowPlace[r[j]]
            xdebug(f"row:解答が1件消えます 列{r[j]} {idx}番目追加({r[idx]},{c[idx]})")
            rowPlace[r[idx]]=0
            columnPlace[c[idx]]=0
            res-=1
        if 0 < columnPlace[c[j]]:
            idx=columnPlace[c[j]]
            xdebug(f"column:解答が1件消えます 行{c[j]} {idx}番目追加({r[idx]},{c[idx]})")
            rowPlace[r[idx]]=0
            columnPlace[c[idx]]=0
            res-=1
        rowPlace[r[j]]=j
        columnPlace[c[j]]=j
        xdebug(f"({r[j]},{c[j]})に追加されました")
        res+=1
    return res

def resolve():
    res=solver()
    print(res)



class TestClass(unittest.TestCase):
    def test_sample1(self):
        input = """3 6
1 1
1 2
3 3
3 2
1 3
1 3"""
        expected = """2"""
        self.judge(input, expected)

    def test_sample2(self):
        input = """2 3
1 2
2 1
1 1"""
        expected = """1"""
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
