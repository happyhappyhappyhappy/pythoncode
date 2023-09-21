import sys

def pow2(n,p):
    ans = 1
    while p > 0:
        if (p & 1) == 1:
            ans = ans*n
        n = n*n
        p = p >> 1
    return ans

n,p = map(int,sys.stdin.readline().split())
x = pow2(n,p)
print(f"pow2({n},{p})={x}")
