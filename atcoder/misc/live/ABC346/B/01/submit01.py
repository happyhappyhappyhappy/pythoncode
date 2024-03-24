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

B_s="wbwbwwbwbwbw"

def solver(W:int,B:int):
    result = "No"
    leng=B+W
    longPiano=B_s*100
    for j in range(12):
        cut_p=longPiano[j:j+leng]
        # xdebug(f"{j=} の時 {cut_p=}")
        cut_b=cut_p.count("b")
        cut_w=cut_p.count("w")
        # xdebug(f"{cut_w=},{cut_b=}")
        if B == cut_b and cut_w == W:
            # xdebug(f"{j=}から切り出したとき 黒鍵 {B} 白鍵 {W}です")
            result="Yes"
            return result
    # algorithm
    return result

if __name__ == "__main__":
    W,B=MI()
    print(f"{solver(W,B)}")
