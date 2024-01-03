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
const ll INF = 1LL << 60;
struct Edge{
    int from;
    int to;
    int cost;
};
void initial(void){
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
}
bool BellmanFord(vector<Edge>& edges,vector<ll>& dist,int V,int start){
    dist[start]=0;
    for(int j=0;j<V;j=j+1){
        bool changed=false;
        for(auto& e:edges){
            if(dist[e.from]==INF){
                continue;
            }
            ll x = dist[e.from]+e.cost;
            if(x < dist[e.to]){
                dist[e.to]=x;
                changed=true;
            }
        }
        if(changed == false){
            return false;
        }
    }
    for(int j=0;j<V;j=j+1){
        for(auto& e:edges){
            if(dist[e.from]==INF){
                continue;
            }
            ll x = dist[e.from]+e.cost;
            if(x < dist[e.to]){
                dist[e.to]=INF*(-1);
            }
        }
    }
    return true;
}
int main(void){
    initial();
    int N,M,P;
    cin >> N >> M >> P;
    vector<ll> dist(N,INF);
    vector<Edge> edges(M);
    for(int j=0;j<M;j=j+1){
        int from,to,cost;
        cin >> from >> to >> cost;
        edges[j].from=from-1;
        edges[j].to=to-1;
        edges[j].cost=(cost-P)*(-1);
    }
    BellmanFord(edges,dist,N,0);
    if(dist[N-1]==(-1)*INF){
        cout << "-1\n" << flush;
    }else{
        ll ans=dist[N-1]*(-1);
        if(ans < 0){
            ans=0;
        }
        cout << ans << "\n" << flush;
    }
    return 0;
}
