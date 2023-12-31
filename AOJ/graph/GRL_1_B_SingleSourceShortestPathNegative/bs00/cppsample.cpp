#include<bits/stdc++.h>
#ifdef LOCAL
// #include"/wrk/sakura-cpp/comp_pro/debug.h"
// #include"/wrk/sakura-cpp/comp_pro/t_debug.h"
// #include"/wrk/sakura-cpp/lib/dump.hpp"
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
struct Edge{
    long long from;
    long long to;
    long long cost;
};
using Edges = vector<Edge>;
const long long INF = 1LL<<60;
bool bellman_ford(const Edges &Es,int V,int s,vector<long long> &dis){
    dis.resize(V,INF);
    dis[s]=0;
    int cnt=0;
    while(cnt < V){
        debug("ただいま %d 回目の検索\n",cnt+1);
        bool end=true;
        for(auto& e:Es){
            long long x = dis[e.from]+e.cost;
            if(dis[e.from]!=INF && x < dis[e.to]){
                debug("%lld->%lldにて最適な経路発見\n",e.from,e.to);
                dis[e.to]=x;
                end=false;
            }
        }
        if(end==true){
            debug("%d 回目の検索で終わったので「途中で」抜ける\n",cnt+1);
            break;
        }
        cnt=cnt+1;
    }
    if(cnt==V){
        return true;
    }else{
        return false;
    }

}


void initial(void){
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
}
int main(void){
    initial();
    int V,E,r;
    cin >> V >> E >> r;
    Edges Es;
    for(int j=0;j<E;j=j+1){
        long long s,t,d;
        cin >> s >> t >> d;
        Es.push_back({s,t,d});
    }
    vector<long long> dis;
    if(bellman_ford(Es,V,r,dis)){
        cout << "NEGATIVE CYCLE\n" << flush;
    }else{
        for(int j=0;j<V;j=j+1){
            if(dis[j]==INF){
                cout << "INF\n" << flush;
            }else{
                cout << dis[j] << "\n" << flush;
            }
        }
    }
    return 0;
}
