N,K = map(int,input().split())
A = list(map(int,input().split()))

def is_ok(t):
    # tの長さで切ったとき,Kより大きくなるかどうか
    logs = 0

    for a in A:
        logs_b=logs
        x = (-a)//t
        x2 = a//t
        print(f"{a}を長さ{t}で切る回数{x}*(-1),これと-を抜いて±相殺にすると{x2}")
        if not ((x*(-1))==x2):
            print(f"\t相殺結果が合わない!!")
        logs=logs+(-(x))
        print(f"\t{logs_b}->{logs}")
    print(f"\tK={K},と比較したい数logs-N={logs}-{N}={logs-N}")
    return logs-N <= K

def meguru_bisect(ng,ok):
    while(1 < abs(ok-ng)):
        mid = (ok+ng)//2
        if is_ok(mid):
            print(f"{mid}はOKなので{ok}の値を下げる")
            ok = mid
        else :
            print(f"{mid}はNGなので{ng}の値を上げる")
            ng = mid
    return ok

print(meguru_bisect(0,10**9+1))
