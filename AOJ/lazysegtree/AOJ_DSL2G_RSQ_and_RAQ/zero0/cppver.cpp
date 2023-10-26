#include<bits/stdc++.h>
#ifdef LOCAL
#include"/wrk/cdebug/debug.h"
#include"/wrk/cdebug/t_debug.h"
#else
#define debug(...) 42
#define debug2(...) 42
#define debugt(...) 42
#define to_string(...) 42
#define debug_out(...) 42
#endif
using namespace std;
using ll=long long int;
const double pi = 3.141592653589793238;
const int yamaMAX_INT = 1 << 29;
const ll yamaMAX_LL = 1LL << 60;
int N,Q;
struct LazySegmentTree{
    private:
    int n;
    vector<ll> node,lazy;
    public:
    LazySegmentTree(vector<ll> v){
        int sz=(int)v.size();
        n = 1;
        while( n < sz){
            n = n*2;
        }
        node.resize(2*n-1);
        lazy.resize(2*n-1,0);
        for(int j=0;j<sz;j=j+1){
            node[(n-1)+j]=v[j];
        }
        for(int j=n-2;j >= 0;j=j-1){
            node[j]=node[j*2+1]+node[j*2+2];
        }
    }
    void eval(int k,int l,int r){
        debug("k = %d,l = %d,r = %dの場合を評価します\n",k,l,r);
        if(lazy[k]!=0){
            node[k]=node[k]+lazy[k];
            if(1 < r-l){
                debug("lazy[%d,%d]+lazy[%d]/2=%lld+%lld\n",2*k+1,2*k+2,k,lazy[2*k+1],lazy[k]/2);
                lazy[2*k+1]=lazy[2*k+1]+lazy[k]/2;
                lazy[2*k+2]=lazy[2*k+2]+lazy[k]/2;
            }
            lazy[k]=0;
        }
    }
    void add(int a,int b,ll x,int k=0,int l=0,int r=-1){
        debug("exe next add(%d,%d,%lld) start!\n",a,b,x);
        debug("exe add(%d,%d,%lld,%d,%d,%d)\n",a,b,x,k,l,r);
        if(r<0){
            r = n;
        }
        eval(k,l,r);
        if(b <= l || r <= a){
            return;
        }
        if(a <= l && r <= b){
            debug("lazy[%d]=lazy[%d]+(%d-%d)*%lld\n",k,k,r,l,x);
            lazy[k]=lazy[k]+(r-l)*x;
            eval(k,l,r);
        }
        else{
            add(a,b,x,2*k+1,l,(l+r)/2);
            add(a,b,x,2*k+2,(l+r)/2,r);
            node[k]=node[2*k+1]+node[2*k+2];
        }

    }
    ll getsum(int a,int b,int k=0,int l=0,int r=-1){
        if(r < 0){
            r = n;
        }
        eval(k,l,r);
        if(b <= l || r <= a){
            return 0;
        }
        if(a <= l && r <= b){
            debug("突破しました。今の k = %dを返します\n",k);
            return node[k];
        }
        debug("getsum(%d,%d,%d,%d,%d)",a,b,2*k+1,l,(l+r)/2);
        ll vl=getsum(a,b,2*k+1,l,(l+r)/2);
        ll vr=getsum(a,b,2*k+2,(l+r)/2,r);
        return vl+vr;
    }
};

void initial(void){
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
}
int main(void){
    initial();
    cin >> N >> Q;
    LazySegmentTree seg(vector<ll>(N,0));
    for(int j=0;j<Q;j=j+1){
        int query;
        cin >> query;
        if(query == 0){
            int s,t,x;
            cin >> s >> t >> x;
            debug("Queue %d to %d , plus %d\n",s-1,t,x);
            seg.add(s-1,t,x);
        }
        else{
            int s,t;
            cin >> s >> t;
            ll ans;
            ans = seg.getsum(s-1,t);
            cout << ans  << endl;
        }
    }
    return 0;
}
