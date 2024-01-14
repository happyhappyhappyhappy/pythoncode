#!/usr/bin/env python3


def shrink_coordinate(a):
    b = sorted(list(set(a)))
    table = {v: k for k, v in enumerate(b)}

    return list(map(lambda x: table[x], a))


N, M = list(map(int, input().split()))

X = [[] for _ in range(N)]
P = [0 for _ in range(M)]
Y = [0 for _ in range(M)]

for i in range(M):
    P[i], Y[i] = [int(x) for x in input().split()]
    X[P[i] - 1].append(Y[i])

shrink_X = [[] for _ in range(N)]
for i in range(N):
    shrink_X[i] = shrink_coordinate(X[i])

idx = [0 for _ in range(N)]

for i in range(M):
    p = P[i]
    num = shrink_X[p - 1][idx[p - 1]] + 1
    idx[p - 1] += 1
    print("{:06d}{:06d}".format(p, num))
