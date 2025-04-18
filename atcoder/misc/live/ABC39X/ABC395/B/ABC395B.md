# ABC395B

[本文](https://atcoder.jp/contests/abc395/tasks/abc395_b)
[解説](https://atcoder.jp/contests/abc395/editorial/12289)
[回答](https://atcoder.jp/contests/abc395/submissions/63750391)

- 灰色200点
- 難易度72
- 回答確率70パーセント
- 回答時間21min

## 図面の作り方

```python3
    F=[["?"] * N for _ in range(N)]
```

## 解説

- 本文通りに処理すれば良い
- ただ、各種変数が1indexでpython3では0indexなのでそれを修正

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

def makeField(N):
    res=[["#"]*N for _ in range(N)]
    return res

def solver():
    res = [["#"]*2 for _ in range(2)]
    # algorithm
    N=II()
    res=makeField(N)
    for i in range(1,N+1):
        j=N+1-i
        if i <= j:
            ch="?"
            if i % 2 == 1:
                ch="#"
            else:
                ch="."
        for x in range(i,j+1):
            for y in range(i,j+1):
                res[x-1][y-1]=ch
    return res


if __name__ == "__main__":
    res=solver()
    N=len(res)
    for x in res:
        xstr="".join(x)
        print(xstr,flush=True)

```
