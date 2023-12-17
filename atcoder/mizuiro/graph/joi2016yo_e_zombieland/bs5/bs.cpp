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
typedef long long ll;
typedef pair<ll,ll> P;
#define INF (1LL << 60)
vector<ll> edge[108000];
ll dist[108000];
bool zombie[108000];
bool danger[108000];
ll pcost,qcost;
ll n,m,k,s,x,a,b;

void dijkstra(ll start){
    priority_queue<P,vector<P>,greater<P>> pq;
    fill(dist,dist+108000,INF);
    dist[start]=0;
    pq.push(P(0,start));
    while(pq.empty()==false){
        P tmp=pq.top();
        pq.pop();
        ll from = tmp.second;
        ll d=tmp.first;
        if(dist[from] < d){
            continue;
        }
        for(ll j=0;j<ll(edge[from].size());j=j+1){
            ll to = edge[from][j];
            if(zombie[to]==true){
                continue;
            }
            ll cost=pcost;
            if(danger[to]==true){
                cost=qcost;
            }
            if(to == n){
                cost=0;
            }
            if(dist[from]+cost < dist[to]){
                dist[to]=dist[from]+cost;
                pq.push(P(dist[to],to));
            }
        }
    }
}
bool done[108000];
vector<ll> edges[108000];

int main(void){
    cin >> n >> m >> k >> s;
    cin >> pcost >> qcost;
    queue<ll> q;
    for(ll j=0;j<k;j=j+1){
        cin >> x;
        zombie[x]=true;
        q.push(x);
    }
    for(ll j=0;j<m;j=j+1){
        cin >> a >> b;
        edge[a].push_back(b);
        edge[b].push_back(a);
    }
    for(ll j1=0;j1<=s;j1=j1+1){
        debug("ゾンビの範囲 %lld での探索をします\n",j1);
        if(q.empty()==true){
            break;
        }
        for(ll j=ll(q.size()-1);0<=j;j=j-1){
            ll from=q.front();
            q.pop();
            if(danger[from]==true){
                continue;
            }
            debug("%lld を危険としてマークしました\n",from);
            danger[from]=true;
            for(ll k=0;k<(ll)edge[from].size();k=k+1){
                q.push(edge[from][k]);
            }
        }
    }
    debug("危険かどうか\n");
    for(int j=1;j<n+1;j=j+1){
        if(danger[j]==true){
            debug("%d -> 危険\n",j);
        }
        else{
            debug("%d -> 安全\n",j);
        }
    }
    dijkstra(1LL);
    cout << dist[n] << endl;
    return 0;
}
