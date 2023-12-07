# 初期値は10
initial_value = 10

# 3列2行のリストを作成
D = [[[initial_value] for _ in range(3)] for _ in range(2)]

# 初期化の後に2箇所変更
D[0][1] = 3
D[1][2] = 2

# 各行の最小値を求める
min_values = [min(row) for row in D]

# 結果を表示
for i, x in enumerate(min_values):
    print(f"Minimum value in row {i}: {x}")
