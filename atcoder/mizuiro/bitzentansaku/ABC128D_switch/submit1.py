import sys
# from collections import defaultdict
# import heapq,copy
import pprint as pp
# from collections import deque
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]

# Const
MAXSIZE = ( 1 << 31 ) -1
MINSIZE = -( 1 << 31) + 1

N,M = MI() # N->スイッチ M->ランプ
G = list()
for x in range(M):
    G.append(LI())
ODDCHECK = LI()

# 加工
# 各行先頭を削る
for x in range(M):
    G[x]=G[x][1:]
    # 他に G[x].pop(0)
    # del G[x][0]
# print(G)
for x in range(M):
    x_Length = len(G[x])
    for y in range(x_Length):
        G[x][y] = G[x][y]-1
print("0-indexの結果")
# print(G)

for switch_pattern in range(1<<N):
# 各スイッチパターン毎の初期情報
    switch_onofflist = list() # switchのON/OFFチェックリスト

    switch_count = 0
    # switch_onofflistの内容作成
    for bit_shift in range(N):
        if (switch_pattern >> bit_shift) & 1:
            switch_onofflist.append(True)
            switch_count = switch_count+1
        else:
            switch_onofflist.append(False)
    # 押されているswitchの数が奇数か否か
    switch_odd = switch_count % 2
# ランプ毎にこのスイッチパターンで付くか否か確認
# 付いているランプの数
    on_lamp = 0
    for lamp in range(M):
        # TODO: ランプ毎に付くか否か確認。付くならon_lamp++
        # スイッチ対応表が一致＋switch_oddと一致か確認
        # 最後にランプの個数とon_lampの値が一致するか確認
