# --- リファクタリング後のコード ---

def rotate_grid_90_degrees(grid):
    """
    2次元リスト（グリッド）を時計回りに90度回転させる関数。

    Args:
        grid (list[list[str]]): 回転させたいN x Nのグリッド。

    Returns:
        list[list[str]]: 90度回転した後の新しいグリッド。
    解説:
    1. `zip(*grid)`:
       これは行列の「転置」を行うテクニックです。
       行と列を入れ替えます。
       例: [[1, 2], [3, 4]] -> [(1, 3), (2, 4)]
    2. `row[::-1]`:
       転置した後の各行（タプル）を逆順にします。
       例: (1, 3) -> (3, 1)
    3. `[list(row[::-1]) for row in zip(*grid)]`:
       上記の処理をすべての行に対して行い、新しいリストとして再構築します。
       これにより、90度の回転が実現できます。
    """
    # 転置してから各行を反転させると、時計回りに90度回転したことになる
    transposed = zip(*grid)
    rotated_grid = [list(row[::-1]) for row in transposed]
    return rotated_grid


def count_differences(grid_s, grid_t):
    """
    2つのグリッドを比較し、異なる文字の数を数える関数。

    Args:
        grid_s (list[list[str]]): 比較元のグリッド。
        grid_t (list[list[str]]): 比較先のグリッド。

    Returns:
        int: 2つのグリッド間で文字が異なるセルの総数。
    """
    diff_count = 0
    # グリッドのサイズ（N）を取得
    grid_size = len(grid_s)
    # 2重ループですべてのセルをチェック
    for r in range(grid_size):       # r: row (行)
        for c in range(grid_size):   # c: column (列)
            if grid_s[r][c] != grid_t[r][c]:
                diff_count += 1
    return diff_count


def main():
    """
    プログラムのメイン処理を行う関数。
    """
    # --- 1. 入力 ---
    # N（グリッドのサイズ）を整数として受け取る
    n = int(input())
    # グリッドSをN行ぶん受け取り、2次元リストに変換する
    # list(input()) は "##." のような文字列を ['#', '#', '.'] のようなリストに変換する
    grid_s = [list(input()) for _ in range(n)]
    # グリッドTも同様に受け取る
    grid_t = [list(input()) for _ in range(n)]

    # --- 2. 計算 ---
    # 最小コストを保存する変数。最初は非常に大きな値で初期化しておく
    min_cost = float("inf")
    current_s = grid_s
    # 0回、1回、2回、3回の回転を試すループ
    for num_rotations in range(4):
        # コスト(1): 文字を変更する回数
        change_cost = count_differences(current_s, grid_t)
        # コスト(2): 回転させた回数
        rotation_cost = num_rotations
        # 総コスト = 変更コスト + 回転コスト
        total_cost = change_cost + rotation_cost
        # これまでの最小コストよりも今回のコストが小さければ、更新する
        if total_cost < min_cost:
            min_cost = total_cost
        # 次のループのために、グリッドを90度回転させておく
        current_s = rotate_grid_90_degrees(current_s)

    # --- 3. 出力 ---
    print(min_cost)


# このファイルが直接実行されたときにだけ、main()関数を呼び出す
if __name__ == "__main__":
    main()
