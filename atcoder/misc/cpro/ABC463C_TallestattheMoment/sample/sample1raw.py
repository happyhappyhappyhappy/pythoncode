from collections import defaultdict
import bisect

N = int(input())
L_LIST = []
H_LIST = []
for i in range(N):
    H, L = map(int,input().split())
    L_LIST.append(L)
    H_LIST.append(H)
Q = int(input())
T = list(map(int, input().split()))

# 時刻L時点での最大値の値を求めておく
# 身長リスト(H_LIST)を後ろから探索している
max_list = []
current_max = 0
for i in range(N-1, -1, -1):
    current_max = max(H_LIST[i], current_max)
    max_list.append(current_max)
max_list.reverse()
print(max_list)
# Queryを処理
# 時刻t 時点での最高身長をprintする
print(L_LIST)
for i in range(len(T)):
    t = T[i]
    index = bisect.bisect_right(L_LIST, t)
    print(f"{t}のインデックスは {index}です")
    print(max_list[index])
