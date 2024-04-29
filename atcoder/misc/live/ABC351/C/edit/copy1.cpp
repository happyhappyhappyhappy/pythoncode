#include<bits/stdc++.h>
#ifdef LOCAL
#include"/wrk/debug/debug.h"
#include"/wrk/debug/t_debug.h"
#include"/wrk/sakura-cpp/lib/dump.hpp"
#else
#define debug(...) 42
#define debug2(...) 42
#define debugt(...) 42
#define to_string(...) 42
#define debug_out(...) 42
#endif
using namespace std;
using ll=long long;
const double pi = 3.141592653589793238;
const int yamaMAX_INT = 1 << 29;
const ll yamaMAX_LL = 1LL << 60;

void initial(void){
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
}
int main(void){
    initial();
    int N=0;
    int L=0;
    vector<int> A(200000);
    cin >> N;
    for(int j=0;j<N;j=j+1){
        cin >> A[L];
        L=L+1;
        while(1<L){
            if(A[L-2]==A[L-1]){
                ;
            }
        }
    }
    return 0;
}
