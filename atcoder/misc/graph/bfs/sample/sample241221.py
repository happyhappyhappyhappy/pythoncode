from collections import deque

def solve_maze(maze):
    """
    迷路の最短経路を幅優先探索で解くプログラム
    'S': スタート
    'G': ゴール
    '#': 壁
    '.': 通路
    """
    # 迷路の行数と列数を取得
    height = len(maze)
    width = len(maze[0])

    # スタート位置を探す
    start = None
    for i in range(height):
        for j in range(width):
            if maze[i][j] == "S":
                start = (i, j)
                break
        if start:
            break

    # 移動方向（上、右、下、左）
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    # BFSで使用するキューと訪問済み位置の記録
    queue = deque([(start, [])])
    visited = {start}

    while queue:
        print(f"Now queue={queue}")
        (curr_y, curr_x), path = queue.popleft()

        # ゴールに到達した場合
        if maze[curr_y][curr_x] == "G":
            return [*path, (curr_y, curr_x)]

        # 四方向を探索
        for dy, dx in directions:
            next_y, next_x = curr_y + dy, curr_x + dx

            # 迷路の範囲内かチェック
            if 0 <= next_y < height and 0 <= next_x < width:
                # 未訪問かつ壁でない場合
                if (next_y, next_x) not in visited and maze[next_y][next_x] != '#':
                    visited.add((next_y, next_x))
                    queue.append(((next_y, next_x), [*path, (curr_y, curr_x)]))

    return None  # 経路が見つからない場合

# テスト用の迷路
maze = [
    list("S...#"),
    list("#.#.."),
    list("..#.#"),
    list(".#..G")
]

# 迷路を表示
def print_maze(maze, path=None):
    if path is None:
        for row in maze:
            print("".join(row))
    else:
        # パスを'*'で表示
        path_set = set(path)
        for i, row in enumerate(maze):
            for j, cell in enumerate(row):
                if (i, j) in path_set and cell not in "SG":
                    print("*", end="")
                else:
                    print(cell, end="")
            print()

print("元の迷路:")
print_maze(maze)

# 最短経路を探索
path = solve_maze(maze)

if path:
    print("\n最短経路（*で表示）:")
    print_maze(maze, path)
    print(f"\n最短経路の長さ: {len(path)-1}")
else:
    print("\n経路が見つかりませんでした")
