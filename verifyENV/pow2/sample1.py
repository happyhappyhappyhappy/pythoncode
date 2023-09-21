import sys
def pow(x,n):
    ans=1
    while n>0 :
        ns1 = n & 1
        if ns1 == 1:
            ans=ans*x

        x = x*x

        n = n >>1
    return ans

n,b= map(int,sys.stdin.readline().split())
print(f"{n}の{b}乗")
x = pow(n,b)
print(f"解答 {x}")
