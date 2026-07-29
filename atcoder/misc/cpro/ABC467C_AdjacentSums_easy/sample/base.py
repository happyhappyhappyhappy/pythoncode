def main():
    N,M = map(int,input().split())
    lisA = list(map(int,input().split()))
    lisB = list(map(int,input().split()))

    ans = 10**9

    ans_tmp = 0
    lisA_tmp = lisA.copy()
    for i in range(N-1):
        j = N-1-i
        A1 = lisA_tmp[j]
        A2 = lisA_tmp[j-1]
        B = lisB[j-1]
        if (A1+A2)%M != B:
            lisA_tmp[j-1] += 1
            ans_tmp += 1
    ans = min(ans,ans_tmp)

    ans_tmp = 0
    lisA_tmp = lisA.copy()
    lisA_tmp[N-1] += 1
    ans_tmp += 1
    for i in range(N-1):
        j = N-1-i
        A1 = lisA_tmp[j]
        A2 = lisA_tmp[j-1]
        B = lisB[j-1]
        if (A1+A2)%M != B:
            lisA_tmp[j-1] += 1
            ans_tmp += 1
    ans = min(ans,ans_tmp)
    print(ans)

if __name__ == "__main__":
    main()
