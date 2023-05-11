def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = dp(N, A)
    print(ans)

def dp(N : int, A : list):
    dp_table = [ [0] * 21 for _ in range(N - 1)]
    dp_table[0][A[0]] = 1
    for i in range(N - 1):
        a = A[i]
        for j in range(21):
            if 0 <= j + a <= 20:
                dp_table[i][j + a] += dp_table[i - 1][j]
            if 0 <= j - a <= 20:
                dp_table[i][j - a] += dp_table[i - 1][j]
    return dp_table[N - 2][A[N - 1]]

if __name__ == "__main__":
    main()
