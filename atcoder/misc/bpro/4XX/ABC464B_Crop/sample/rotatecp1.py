def rotate(C):
    return ["".join(r) for r in zip(*C[::-1])]

H,W=map(int,input().split(" "))
C=[input() for _ in range(H)]

for _ in range(4):
    while "#" not in C[0]:
        C=C[1:]
    C=rotate(C)

print(C)
