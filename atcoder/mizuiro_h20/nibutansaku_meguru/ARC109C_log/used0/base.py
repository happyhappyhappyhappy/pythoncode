def is_ok(l):
    # n+1で指定された数(1,2,3...)の丸太を作成出来るか
    return N+1 >= l*(l+1)//2

def meguru_bisect(ng, ok):
    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok


N = int(input())
print(N+1-meguru_bisect(10**20, 0))
