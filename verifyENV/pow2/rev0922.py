import sys

def pow2(p,n):
    result=1
    while n > 0:
        n_and_1=n & 1
        if n_and_1 == 1:
            print(f"{p} を掛けます")
            result=result*p
        p=p*p
        n = n >>1
    return result

a,b = map(int,sys.stdin.readline().split())
print(f"{a} の {b} 乗")
ans = pow2(a,b)
print(f"{ans}")
