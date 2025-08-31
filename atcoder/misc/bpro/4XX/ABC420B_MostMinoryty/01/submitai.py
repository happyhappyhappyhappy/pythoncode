import sys

def solver():
    """
    入力されたN行M列の0と1の文字列配列から、各行のスコアを計算し、
    最高スコアの行番号を返す関数。
    """
    # N行M列のサイズを取得
    try:
        num_rows, num_cols = map(int, sys.stdin.readline().split())
    except ValueError:
        return []

    # 0と1の文字列配列を読み込む
    data_matrix = [sys.stdin.readline().strip() for _ in range(num_rows)]
    print(f"data_matrix={data_matrix}")
    # 各行のスコアを格納するリスト
    scores = [0] * num_rows

    # 各列ごとに0と1の少ない方のグループにスコアを加算
    for col_index in range(num_cols):
        # 0と1の行インデックスを分類
        zero_indices = [row_idx for row_idx, row_str in enumerate(data_matrix) if row_str[col_index] == '0']
        one_indices = [row_idx for row_idx, row_str in enumerate(data_matrix) if row_str[col_index] == '1']

        # 少ない方のグループを選択
        if len(zero_indices) <= len(one_indices):
            target_indices = zero_indices
        else:
            target_indices = one_indices

        # 選択したグループのスコアを加算
        for idx in target_indices:
            scores[idx] += 1
    max_score = max(scores)

    # 最高スコアの行番号（1から始まる）を取得
    result_rows = [i + 1 for i, score in enumerate(scores) if score == max_score]

    return result_rows

if __name__ == "__main__":
    result = solver()
    print(*result)
