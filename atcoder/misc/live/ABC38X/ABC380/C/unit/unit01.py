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
    res=[("0",1),("1",1)]
    j=0
    res=list()
    while j < N:
        k=j
        ch=S[j]
        while k < N and S[k] == ch:
            k+=1
        cnt=k-j
        j=k
        res.append((ch,cnt))
    return res,len(res)
def tuple2str(tup):
    ch,cnt=tup
    res=ch*cnt
    return res

def solver():
    res="001001001001"
    N,K=MI()
    S=input().rstrip()
    xdebug(f"N={N},K={K},S={S}")
    RL,RL_LEN=runlength(N,S)
    xdebug(f"RL={RL},RL LEN={RL_LEN}")
    # 位置交換
    # K 番目の位置探し
    oneLst=list()
    for j in range(RL_LEN):
        ch,_=RL[j]
        if ch == "1":
            oneLst.append(j)
    xdebug(f"「1」がある番目は1-indexで{oneLst}")
    xdebug(f"したがって0-index で{oneLst[K-1]}番目の物を持ってくればいい")
    sw=oneLst[K-1]
    tmp=RL[sw]
    RL[sw]=RL[sw-1]
    RL[sw-1]=tmp
    xdebug(f"結果のrunlength {RL}")
    res=""
    for j in range(RL_LEN):
        tup=RL[j]
        st=tuple2str(tup)
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
