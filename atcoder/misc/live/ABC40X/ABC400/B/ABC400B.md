# ABC400B

## 問題情報

- [本文](https://atcoder.jp/contests/abc400/tasks/abc400_b)
- [解説](https://atcoder.jp/contests/abc400/editorial/12623)
- [回答](https://atcoder.jp/contests/abc400/submissions/64585240)

## 回答

```python3
# ライブラリのインポート
import pprint as pp
import sys
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

# ちょっと冗長じゃない？**演算子で十分だよ！
def pow2(P:int,N:int)->int:
    res=1
    while 0 < N:
        nand1=N & 1
        if nand1 == 1:
            res=res*P
        P=P*P
        N=N>>1
    return res

def solver():
    res = 0
    # algorithm
    N,M=MI()
    # THISMAXって変数名、ちょっと紛らわしいかも？上限値って意味ならUPPER_BOUNDとかの方が分かりやすいかも！
    UPPER_BOUND=10**9
    for j in range(M+1):
        # ここも**演算子で書けるね！
        x=N**j
        res=res+x
        if UPPER_BOUND < res:
            return "inf"
    return res


if __name__ == "__main__":
    print(solver())


```
