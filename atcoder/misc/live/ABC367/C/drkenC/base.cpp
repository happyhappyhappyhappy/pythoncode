#include <bits/stdc++.h>
using namespace std;

void dfs(vector<int> &A, int K, const vector<int> &R, int sum) {
    // 終端条件 --- N 回までいったら終わり
    if (A.size() == R.size()) {
        if (sum % K == 0) {
            for (int i = 0; i < A.size(); ++i) cout << A[i] << " ";
            cout << endl;
        }
        return;
    }

    for (int v = 1; v <= R[A.size()]; ++v) {
        A.push_back(v);
        dfs(A, K, R, sum + v);
        A.pop_back(); // これが結構ポイント
    }
}

int main() {
    int N, K;
    cin >> N >> K;
    vector<int> R(N);
    for (int i = 0; i < N; ++i) cin >> R[i];

    vector<int> A;
    dfs(A, K, R, 0);
}
