import sys

def solve():
    # 1. 入力の受け取り
    # 標準入力から1行読み込み、空白で分割して整数に変換
    line = sys.stdin.readline().split()
    if not line:
        return
    n, m = map(int, line)
    # グリッド（盤面）をリストに格納
    grid = [sys.stdin.readline().strip() for _ in range(n)]

    # 2. 部分グリッドを抽出して保存するセット（重複を除外するため）
    unique_subgrids = set()

    # 3. M x M の範囲をスライスして取り出す
    # 外側のループ：開始位置の行 (i)
    for i in range(n - m + 1):
        # 内側のループ：開始位置の列 (j)
        for j in range(n - m + 1):
            # 指定された範囲の行を取り出し、さらに横方向をスライス
            # tupleにするのは、setに入れるために「変更不可（ハッシュ可能）」にする必要があるため
            subgrid = []
            for row_index in range(i, i + m):
                subgrid.append(grid[row_index][j : j + m])
            # リストをタプルに変換してセットに追加
            unique_subgrids.add(tuple(subgrid))

    # 4. 結果の出力（セットの長さ ＝ 種類の数）
    print(len(unique_subgrids))

if __name__ == "__main__":
    solve()
