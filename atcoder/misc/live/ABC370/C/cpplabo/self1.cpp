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
    string S,T;
    cin >> S >> T;
    vector<string> ans;
    int n = (int)S.size();
    while (S != T){
        debug2("今のS: %s\n",S.c_str());
        string nxt(n,'z');
        debug2("次の値 : %s\n",nxt.c_str());
        for(int j = 0;j<n;j+=1){
            if(S[j]!=T[j]){
                string tmp=S;
                tmp[j]=T[j];
                debug2("nxt=%s と tmp=%sを比較\n",nxt.c_str(),tmp.c_str());
                nxt=min(nxt,tmp);
                debug2("if文 次の結果 : %s\n",nxt.c_str());

            }
        }
        debug2("%s を答えに入れる\n",nxt.c_str());
        ans.push_back(nxt);
        S=nxt;
    }
    int sz=(int)ans.size();
    cout << sz << "\n";
    for(string e:ans)
    {
        cout << e << "\n";
    }
    return 0;
}
