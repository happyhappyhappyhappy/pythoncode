# ABC399B

## 問題情報

- [本文](https://atcoder.jp/contests/abc399/tasks/abc399_b)
- [解説](https://atcoder.jp/contests/abc399/editorial/12563)
- [回答](https://atcoder.jp/contests/abc399/submissions/64865298)

## 解き方

愚直に解いても大丈夫

## 回答

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

def solver():
    N=II()
    res = [-1]*N
    # algorithm
    A=LI()
    r = 1
    while -1 in res:
        # 順位がデフォルトでない物の最大値を求める
        max_val=-1
        for j in range(N):
            if res[j] == -1 and max_val <= A[j]:
                max_val=A[j]
        count=0
        for j in range(N):
            if max_val == A[j]:
                res[j]=r
                count+=1
        r+=count
    return res


if __name__ == "__main__":
    res=solver()
    for x in res:
        print(x)

```

リファクタリングバージョン

```python3
import sys
from logging import DEBUG, StreamHandler, getLogger

def II(): return int(sys.stdin.readline())
def LI(): return list(map(int, sys.stdin.readline().split()))

logger = getLogger(__name__)
handler = StreamHandler()
handler.setLevel(DEBUG)
logger.setLevel(DEBUG)
logger.addHandler(handler)
logger.propagate = False

xdebug = logger.debug

def solve():
    N = II()
    A = LI()
    res = [-1] * N
    rank = 1  # 順位を管理する変数をrankに変更

    while -1 in res:
        max_val = -1
        for i in range(N):
            if res[i] == -1 and A[i] > max_val: #最大値の更新条件を見直し
                max_val = A[i]

        count = 0
        for i in range(N):
            if A[i] == max_val:
                res[i] = rank
                count += 1
        rank += count #順位の更新
    return res

if __name__ == "__main__":
    result = solve() #変数名をresからresultに変更
    for r in result: #変数名をxからrに変更
        print(r)

```
