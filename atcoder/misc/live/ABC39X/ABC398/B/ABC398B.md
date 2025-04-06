# ABC398B

## 問題情報

- [本文](https://atcoder.jp/contests/abc398/tasks/abc398_b)
- [解説](https://atcoder.jp/contests/abc398/editorial/12499)
- [回答](https://atcoder.jp/contests/abc398/submissions/64369850)

## 解き方

bit全探索を使ってみる

- まず5つの数を取り出す値を洗い出す→cant
- この中でカード情報を辞書クラスnumsRに書き出す
- ソートする。尚、いきなりソートできない。非破壊なsortedを使うnumsに入れる
- 長さが2の物についてそれぞれ要素が3,2であることを確認する
- OKならばYesを返す

```python3
# ライブラリのインポート
# import heapq,copy
import pprint as pp
import sys

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

def builtFlug(j,k):
    if (j & (1<<k)) == 0:
        return False
    return True

def solver():
    result = "No"
    # algorithm
    N=7
    A=LI()
    cand=[]
    for j in range(1<<N):
        count = 0
        for k in range(N):
            if builtFlug(j,k):
                count+=1
        if count == 5:
            cand.append(j)
#    xdebug(f"cand={cand}")
    for j in cand:
        numsB={}
        for k in range(N):
            card=A[k]
            if builtFlug(j,k):
                if card in numsB:
                    numsB[card]+=1
                else:
                    numsB[card]=1
        nums=sorted(numsB.items(),key=lambda info:info[1])
#        xdebug(f"{j}->{nums}->{len(nums)}")
        if len(nums) == 2:
            if nums[0][1] == 2 and nums[1][1] == 3:
#                xdebug("Hakkenn")
                return "Yes"
    return result

if __name__ == "__main__":
    print(solver())

```
