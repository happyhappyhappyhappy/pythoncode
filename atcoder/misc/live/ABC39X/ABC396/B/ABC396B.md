# ABC396B

## 基本情報

- [本文](https://atcoder.jp/contests/abc396/tasks/abc396_b)
- [解説](https://atcoder.jp/contests/abc396/editorial/12389)
- [回答例](https://atcoder.jp/contests/abc396/submissions/63756037)

## 二つの標準入力と一つの標準入力がありうるケース

```python3
    queue = tuple(map,input().split(" "))
        if queue[0] == 1:
            _,x=queue # 2個目を取り出す
            cards.append(x)
        else:
            # 省略
```

## リストにLIFO(Last In First Out)したいとき

```python3
    # Last In
    list.append(x)
    # First Out
    x  = list.pop()
```

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
    result = []
    cards=[0]*100
    Q=II()
    for _ in range(Q):
        queue=tuple(map(int,input().split(" ")))
        if queue[0] == 1:
            _,x=queue
            cards.append(x)
        else:
            result.append(cards.pop())
    # algorithm
    return result


if __name__ == "__main__":
    res=solver()
    for x in res:
        print(x)

```
