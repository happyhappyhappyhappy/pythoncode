def main():
    n=int(input())
    s=set(i+1 for i in range(1,2*n+1))
    print(1)
    for _ in range(n+1):
        k=int(input())
        s.discard(k)
        for j in range(2,2*n+2):
            if j in s:
                print(j)
                s.discard(j)
                break

main()
