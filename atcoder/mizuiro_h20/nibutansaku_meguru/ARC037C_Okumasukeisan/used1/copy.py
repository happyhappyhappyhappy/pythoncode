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
    print(f"今チェックしようとしている値 {X}")
    print(f"検索しようとしている数列{A}")
    cnt = 0
    for a in A:
        aa = X // a
        print(f"{B}の中に{aa}より小さい個数を求めたい")
        pos=bisect_right(B,aa)
        print(f"この場合{pos}個")
        cnt = cnt+pos
    result = (K <= cnt)
    if result:
        print(f"数えた結果{cnt} が{K}番目より上 OK")
    else:
        print(f"数えた結果{cnt} が{K}より下 NG")
    return result

def meguru_bisect(ng,ok):
    while (abs(ok-ng)>1):
        mid = ( ok+ng )//2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok
print(meguru_bisect(-1,10**18+1))
