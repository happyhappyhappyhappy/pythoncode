import sys
# import heapq, copy # 未使用のためコメントアウト
# from collections import deque # 未使用のためコメントアウト
import pprint as pp
import logging
from typing import List, Callable, Iterator, Any # 型ヒントの追加

# --- 1. 定数とロギング設定 ----------------------------------------------------

# 定数: 通常のPythonの慣習に従い、定数名はすべて大文字とアンダースコアで記述
# 巨大な数を示す定数として、MAX_INT/MIN_INTなど意図が伝わる名前に変更
INF = float('inf')  # 無限大としてfloat('inf')を使用するのが一般的
# MIN_INF = float('-inf') # 今回のコードでは未使用

# ロギング設定の簡略化
# スクリプト実行時のみデバッグログを出力する設定
logger = logging.getLogger(__name__)
if logger.level == logging.NOTSET:
    handler = logging.StreamHandler()
    handler.setLevel(logging.DEBUG)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(handler)
    logger.propagate = False

# デバッグ用エイリアス
# logger.debugをxdebug、pp.pprintをpppとするのは、短いコードでは冗長なため省略。
# 必要であれば、そのままlogger.debugやpp.pprintを使う方が一般的です。
# debug_print = logger.debug 

# --- 2. 入力ヘルパー関数 ------------------------------------------------------

# 標準入力から1行読み込む基本関数
READLINE: Callable[[], str] = sys.stdin.readline

# 1つの整数を入力 (II -> read_int)
def read_int() -> int:
    """標準入力から1つの整数を読み込む"""
    return int(READLINE())

# 1つの文字列を入力 (SI -> read_str)
def read_str() -> str:
    """標準入力から1つの文字列を読み込む（末尾の改行を削除）"""
    return READLINE().strip()

# 複数の整数をスペース区切りで入力し、Iterator[int]として返す (MI -> read_map_int)
def read_map_int() -> Iterator[int]:
    """標準入力からスペース区切りの整数列を読み込み、mapオブジェクト（イテレータ）を返す"""
    return map(int, READLINE().split())

# 複数の整数をスペース区切りで入力し、リスト[int]として返す (LI -> read_list_int)
def read_list_int() -> List[int]:
    """標準入力からスペース区切りの整数列を読み込み、リストを返す"""
    return list(read_map_int())

# 複数行の整数リストを入力 (LLI -> read_list_of_lists_int)
def read_list_of_lists_int(rows_number: int) -> List[List[int]]:
    """指定された行数分の整数リストを読み込む"""
    return [read_list_int() for _ in range(rows_number)]

# --- 3. 問題の核となる処理 -----------------------------------------------------

def calculate_digit_sum(number: Any) -> int:
    """
    与えられた数（または文字列）の各桁の合計を計算する。
    例: calculate_digit_sum(123) -> 6
    """
    # numberを文字列に変換し、各文字（桁）を整数に変換して合計
    return sum(int(digit) for digit in str(number))

def generate_sequence(max_length: int = 101) -> List[int]:
    """
    A[j] = Σ_{k=0}^{j-1} (各桁の和(A[k])) となる数列Aを生成する。
    
    A[0] = 1
    A[j] = sum(calculate_digit_sum(A[k]) for k in 0 to j-1)
    
    Args:
        max_length: 生成する数列の長さ（インデックス0からmax_length-1まで）
    
    Returns:
        生成された数列A
    """
    # 配列のサイズを明確にするため、max_length + 1ではなくmax_lengthを使用
    sequence = [0] * max_length 
    sequence[0] = 1 # 初期値

    # sequence[j] を計算
    for j in range(1, max_length):
        current_sum_of_digit_sums = 0
        # sequence[j] は k=0 から j-1 までのA[k]の桁和の合計
        for k in range(j):
            # 桁和を計算し、合計に追加
            current_sum_of_digit_sums += calculate_digit_sum(sequence[k])
            
        sequence[j] = current_sum_of_digit_sums
        
    return sequence

def solver():
    """
    数列を生成し、標準入力から受け取ったインデックスXに対するA[X]を返すメインロジック。
    """
    # 問題の制約に合わせて、必要な配列サイズ（0から100のインデックス）で数列を生成
    # 0 <= X <= 100 と仮定し、長さ101の配列を生成
    MAX_INDEX = 101 # インデックス0から100までが必要なので、長さは101
    
    # 数列の生成
    a_sequence = generate_sequence(MAX_INDEX)
    # logger.debug(f"生成された数列 A: {a_sequence}") # デバッグ出力例

    # ユーザーが求めるインデックスXを読み込む (II -> read_int)
    try:
        x_index = read_int()
    except EOFError:
        # EOF（入力終了）の場合は処理を中断
        logger.error("入力がありません。")
        return None
    except ValueError:
        logger.error("入力が整数ではありません。")
        return None

    # インデックスの範囲チェック
    if 0 <= x_index < MAX_INDEX:
        # 結果を返す
        return a_sequence[x_index]
    else:
        # 不正なインデックスの場合
        logger.error(f"入力されたインデックスX={x_index}は範囲[0, {MAX_INDEX-1}]外です。")
        return None

# --- 4. エントリポイント ------------------------------------------------------

if __name__ == "__main__":
    result = solver()
    if result is not None:
        print(result)
