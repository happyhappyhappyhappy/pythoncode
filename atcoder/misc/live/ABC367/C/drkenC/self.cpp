#include<bits/stdc++.h>
#ifdef LOCAL
#include"/wrk/debug/debug.h"
#include"/wrk/debug/t_debug.h"
#else
#define debug(...) 42
#define debug2(...) 42
#define debugt(...) 42
#define to_string(...) 42
#define debug_out(...) 42
#endif
using namespace std;
using ll=long long;
using pint=pair<int,int>;
const double pi = 3.141592653589793238;
const int yamaMAX_INT = 1 << 29;
const ll yamaMAX_LL = 1LL << 60;

void initial(void){
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
}
void dfs(int N,vector<int> &A,int K,vector<int> &R,int sum){
    debug("現在のA\n");
    for(int j=0;j<(int)A.size();j+=1){
        debug("%d ",A[j]);
    }
    debug("\n");
    if((int)A.size()==N){
        if(sum%K==0){
            for(int j=0;j<N;j+=1){
                cout << A[j];
            }
            cout << endl;
        }
        return;
    }
    for(int j=1;j<=R[(int)A.size()];j+=1){
        A.push_back(j);
        dfs(N,A,K,R,sum+j);
        A.pop_back();
    }
}
int main(void){
    initial();
    int N,K;
    cin >> N >> K;
    vector<int> R(N);
    for(int j=0;j<N;j+=1){
        cin >> R[j];
    }
    for(int j=0;j<N;j+=1){
        debug("%d ",R[j]);
    }
    debug("\n");
    vector<int> A;
    dfs(N,A,K,R,0);
    return 0;
}
