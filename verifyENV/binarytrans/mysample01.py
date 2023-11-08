# ライブラリのインポート
import sys
# import heapq,copy
import pprint as pp
# from collections import deque
# pypy3用
# import pypyjit
# 再帰制御解放
# pypyjit.set_param('max_unroll_recursion=-1')
# sys.setrecursionlimit(10**6)
from logging import getLogger, StreamHandler, DEBUG

# 入力のマクロ
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]

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


def decimal_to_binary_array(number):
    if number < 0:
        raise ValueError("正の整数を入力してください")

    if number == 0:
        return [0]

    binary = []
    while number > 0:
        # 一番先頭に入力していく
        binary.insert(0, number % 2)
        number //= 2

    return binary

# 使用例
Q = II()
for j in range(0,Q):
    number = II()
    binary_array = decimal_to_binary_array(number+1)
    print(f"{number} の2進数表現は: {binary_array}")
    bintree = binary_array[1:]
    print(f"動き方は: {bintree}")
