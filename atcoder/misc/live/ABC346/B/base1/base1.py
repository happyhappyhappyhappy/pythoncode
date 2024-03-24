W, B = map(int, input().split())

S = "wbwbwwbwbwbw" * 100
for i in range(12):
    T = S[i: i + W + B]
    if T.count('w') == W and T.count('b') == B:
        print("Yes")
        exit()
print("No")
