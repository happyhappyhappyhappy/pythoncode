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

def runlength(N,S):
    res=[('0',3),('1',4)]
    res=list()
    j = 0
    while j < N:
        k=j
        ch=S[k]
        while k < N and ch == S[k]:
            k+=1
        cnt=k-j
        res.append((ch,cnt))
        j=k
    return res,len(res)
def tuple2str(tup):
    ch,cnt=tup
    res=ch*cnt
    return res
def solver():
    res="101010101010"
    N,K=MI()
    S=input().rstrip()
    xdebug(f"N={N},K={K},S={S}")
    RL,RLLEN=runlength(N,S)
    xdebug(f"runlength={RL},rllen={RLLEN}")
    oneRlPos=list()
    for j in range(RLLEN):
        ch,_=RL[j]
        if ch == "1":
            oneRlPos.append(j)
    xdebug(f"1の塊は {oneRlPos} 番目にある。")
    xdebug(f"runleng->{RL}の {oneRlPos[K-1]}番目にある物を交換すれば良い")
    xdebug(f"交換前")
    for j in range(RLLEN):
        xdebug(f"{RL[j]}")
    mainPos=oneRlPos[K-1]
    RL[mainPos-1],RL[mainPos]=RL[mainPos],RL[mainPos-1]
    xdebug(f"交換後")
    for j in range(RLLEN):
        xdebug(f"{RL[j]}")

    res=""
    for j in range(RLLEN):
        x=RL[j]
        st=tuple2str(x)
        res+=st
    return res

def resolve():
    print(solver())

class TestClass(unittest.TestCase):
    def test_sample1(self):
        input = """15 3
010011100011001"""
        expected = """010011111000001"""
        self.judge(input, expected)

    def test_sample2(self):
        input = """10 2
1011111111"""
        expected = """1111111110"""
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
