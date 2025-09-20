# ライブラリのインポート
import sys

# 入力用関数を定義
def read_input():
    """標準入力からN, Mとグリッドの情報を読み込む"""
    try:
        N, M = map(int, sys.stdin.readline().split())
        grid_rows = [sys.stdin.readline().strip() for _ in range(N)]
        return N, M, grid_rows
    except (IOError, ValueError) as e:
        print(f"入力エラー: {e}", file=sys.stderr)
        return None, None, None

def solve():
    """
    グリッドの各セルをチェックし、特定の条件を満たすか判定する。
    """
    N, M, grid_rows = read_input()
    if N is None:
        return "No"

    # グリッドの周囲を '.' で囲んで境界チェックを簡略化する
    # これは「パディング」と呼ばれるテクニックです
    padded_grid = []
    # 上部のパディング行を追加
    padded_grid.append("." * (M + 2))
    # 元のグリッドの各行をパディングして追加
    for row in grid_rows:
        padded_grid.append("." + row + ".")
    # 下部のパディング行を追加
    padded_grid.append("." * (M + 2))

    # パディングされたグリッドをリストのリストに変換
    grid = [list(row) for row in padded_grid]

    # グリッド全体をループして各セルをチェック
    for r in range(1, N + 1):
        for c in range(1, M + 1):
            # 現在のセルが '#' かどうかを確認
            if grid[r][c] == "#":
                # '#' に隣接する '#' の数をカウント
                neighbor_count = 0
                # 上下左右の4方向をチェック
                if grid[r - 1][c] == "#": neighbor_count += 1
                if grid[r + 1][c] == "#": neighbor_count += 1
                if grid[r][c - 1] == "#": neighbor_count += 1
                if grid[r][c + 1] == "#": neighbor_count += 1

                # 隣接する '#' の数が2か4でない場合、条件を満たさない
                if neighbor_count not in {2, 4}:
                    return "No"
    
    # すべての '#' が条件を満たした場合
    return "Yes"

# メイン処理
if __name__ == "__main__":
    result = solve()
    print(result)