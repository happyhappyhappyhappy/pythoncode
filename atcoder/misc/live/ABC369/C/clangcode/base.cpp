#include <bits/stdc++.h>
using namespace std;

int main() {
    int N;
    cin >> N;
    vector<long long> A(N), B(N-1);
    for (int i = 0; i < N; i++) cin >> A[i];
    for (int i = 0; i + 1 < N; i++) B[i] = A[i+1] - A[i];

    long long res = 0, num = 0;
    for (int i = 0; i < B.size(); ) {
        int j = i;
        while (j < B.size() && B[j] == B[i]) j++;

        long long n = j - i;
        res += (n + 2) * (n + 1) / 2;
        num++;  // 区間の個数

        i = j;
    }
    cout << res - (num - 1) << endl;
}
