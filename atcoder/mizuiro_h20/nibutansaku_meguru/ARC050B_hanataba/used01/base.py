R,B = map(int, input().split())
x,y = map(int, input().split())

def is_ok(bouquet):
    # 指定された数の花束を作れるかチェック
    R_=R-bouquet
    B_=B-bouquet
    if R_<0 or B_<0:
        return False
    return R_//(x-1)+B_//(y-1)>=bouquet

def meguru_bisect(ng, ok):
    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok

print(meguru_bisect(10**20 + 1, 0))
