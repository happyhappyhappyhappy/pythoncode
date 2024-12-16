#include<bits/stdc++.h>
using namespace std;
const int MAX = 210000;

int main() {
    long long N, A;
    cin >> N;
    vector<long long> nums(MAX, 0);
    for (int i = 0; i < N; i++) {
        cin >> A;
        long long B=A;
        for (long long j = 2; j * j <= A; j++) {
            while (A % (j * j) == 0) {
                A /= j * j;
            }
        }
        cout << B << "の抜け殻" << A << endl;
        nums[A]++;
    }

    // (0, 他の数) の組の個数
    long long res = N * (N - 1) / 2 - (N - nums[0]) * (N - nums[0] - 1) / 2;

    // 0 を含まない組の個数
    for (long long val = 1; val < MAX; val++) {
        res += nums[val] * (nums[val] - 1) / 2;
    }
    cout << res << endl;
}
