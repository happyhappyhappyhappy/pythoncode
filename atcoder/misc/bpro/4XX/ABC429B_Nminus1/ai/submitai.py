import sys
from typing import List, Tuple

# === 入力ヘルパー関数 ===
# 競技プログラミングなどでよく使う、高速な入力のための関数たち。
# 今回のコードで使われているのは MI() と LI() だけだけど、
# 他はテンプレートから消してスッキリさせちゃった！

def MI() -> Tuple[int, ...]:
    """標準入力から空白区切りの整数値を読み込み、タプルで返す。"""
    return map(int, sys.stdin.readline().split())

def LI() -> List[int]:
    """標準入力から空白区切りの整数値を読み込み、リストで返す。"""
    return list(MI())

# === メインロジック ===

def solve() -> str:
    """
    問題のメインロジック。
    入力Aの要素の和からMを引いた値が、リストAの中に存在するかを判定する。
    """
    # 最初のNは使ってないから、アンダースコア(_)で無視しちゃお！
    # N, M を受け取る
    _, M = MI()
    # リスト A を受け取る
    A: List[int] = LI()

    # リスト A の要素の合計を計算
    sum_A = sum(A)

    # 探すべき値 (合計から M を引いた値) を計算
    target_value = sum_A - M

    # もし、探すべき値がリスト A の中にあれば "Yes"
    # Pythonの 'in' 演算子は、リスト内に要素があるかを超速でチェックできるよ！
    if target_value in A:
        return "Yes"
    else:
        # なければ "No"
        return "No"

# === 実行部分 ===
if __name__ == "__main__":
    result = solve()
    print(result)