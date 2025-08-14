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
def SI(): return input().rstrip()
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

def calculate_max_t_ratio(text: str) -> float:
    """
    与えられた文字列の中で、両端が 't' で、't' の割合が最も高い部分文字列を探し、その割合を計算するよ。
    Args:
        text: 処理する文字列
    Returns:
        最も高い 't' の割合。見つからない場合は 0.0 を返すよ。
    """
    max_ratio = 0.0
    t_indices = [i for i, char in enumerate(text) if char == "t"]

    # 't'が2つ以上ないと部分文字列が作れないからチェックしとこ
    if len(t_indices) < 2:
        return 0.0

    for i in range(len(t_indices)):
        for j in range(i + 1, len(t_indices)):
            start_index = t_indices[i]
            end_index = t_indices[j]
            xdebug(f"{text[start_index:end_index+1]} について求めます")
           # 't'の個数と部分文字列の長さを計算
            t_count = j - i + 1
            xdebug(f"数は {t_count} 個です")
            substring_length = end_index - start_index + 1
            # 部分文字列の長さが3以上じゃないとダメだよ
            if substring_length >= 3:
                # 割合を計算して、最大値を更新するよ！
                # 両端の 't' を除外するから、-2するの
                ratio = (t_count - 2) / (substring_length - 2)
                max_ratio=max(ratio,max_ratio)
    return max_ratio

def solver():
    res=float(0)
    S=input()
    res=calculate_max_t_ratio(S)
    return res

def resolve():
    res=solver()
    print(res)

class TestClass(unittest.TestCase):
    def test_sample1(self):
        input = """attitude"""
        expected = """0.50000000000000000"""
        self.judge(input, expected)

    def test_sample2(self):
        input = """ottottott"""
        expected = """0.66666666666666667"""
        self.judge(input, expected)

    def test_sample3(self):
        input = """coffeecup"""
        expected = """0.00000000000000000"""
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
