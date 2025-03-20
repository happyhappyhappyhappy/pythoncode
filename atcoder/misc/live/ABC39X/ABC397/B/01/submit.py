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
    res = 0
    # algorithm
    S=input()
    # nxt 次の文字 初期値はi
    nxt="i"
    slen=len(S)
    for j in range(slen):
        s=S[j]
        if s == nxt:
            # もしnxtと一致していれば、中身をiとoで逆転する
            if nxt=="i":
                nxt="o"
            else:
                nxt="i"
        else:
            # もしそうで無ければ挿入する必要があるので1カウント
            res+=1
    if nxt == "o":
        # 最終的にoの場合、oを入れるので1カウント
        res+=1
    return res


if __name__ == "__main__":
    print(solver())
