N, K = map(int, input().split())
A = list(map(int, input().split()))

def is_ok(t):
    # tの長さに切った時、Kより大きくなるかチェック
    logs = 0
    for a in A:
        logs+=-(-a//t)
    return logs-N <= K

def meguru_bisect(ng, ok):
    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok

print(meguru_bisect(0,10**9 + 1))
