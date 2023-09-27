from bisect import bisect_right
import sys
read = sys.stdin.readline

def read_ints():
    return list(map(int,read().split()))

N,K = read_ints()
A = read_ints()
B = read_ints()
A.sort()
B.sort()

def is_ok(X):
    cnt = 0
    for a in A:
        aa = X // a
        cnt += bisect_right(B,aa)
    return cnt >= K

def meguru_bisect(ng,ok):
    while (abs(ok-ng)>1):
        mid = ( ok+ng )//2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok
print(meguru_bisect(-1,10**18+1))
