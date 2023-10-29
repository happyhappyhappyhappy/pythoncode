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
using ll=long long;
const double pi = 3.141592653589793238;
const int yamaMAX_INT = 1 << 29;
const ll yamaMAX_LL = 1LL << 60;
int N,Q;
const int INF =((1<<31)-1);
struct LazySegmentTree{
    private:
        int n;
        vector<int> node;
        vector<int> lazy;
        vector<bool> lazyFlag;
    public:
        LazySegmentTree(vector<int> v){
            int sz=(int)v.size();
            n = 1;
            while ( n < sz ){
                n = n * 2;
            }
            node.resize(2*n-1);
            lazy.resize(2*n-1,INF);
            lazyFlag.resize(2*n-1,false);
            for(int j=0;j<sz;j=j+1){
                node[(n-1)+j]=v[j];
            }
            for(int j=n-2;0 <= j ; j=j-1){
                node[j]=min(node[j*2+1],node[j*2+2]);
            }
        }
        void lazyEvaluate(int k,int l,int r){
            if(lazyFlag[k]==true){
                node[k]=lazy[k];
                if (1 < r - l){
                    lazy[k*2+1]=lazy[k*2+2]=lazy[k];
                    lazyFlag[k*2+1]=lazyFlag[k*2+2]=true;
                }
                lazyFlag[k]=false;
            }
        }
        void update(int a,int b,int x,int k=0,int l=0,int r=-1){
            debug("update(%d,%d,%d,%d,%d,%d)\n",a,b,x,k,l,r);
            if(r < 0){
                r = n;
            }
            debug("->lazyEvaluate(%d,%d,%d)\n",k,l,r);
            lazyEvaluate(k,l,r);
            if(b <= l || r <= a){
                return;
            }
            if(a <= l && r <= b){
                lazy[k]=x;
                lazyFlag[k]=true;
                lazyEvaluate(k,l,r);
            }else{
                update(a,b,x,2*k+1,l,(l+r)/2);
                update(a,b,x,2*k+2,(l+r)/2,r);
                node[k]=min(node[2*k+1],node[2*k+2]);
            }
        }
    int find(int a,int b,int k=0,int l=0,int r=-1){
        if(r<0){
            r = n;
        }
        lazyEvaluate(k,l,r);
        if(b <= l || r <= a){
            return INF;
        }
        if(a <= l && r <= b){
            return node[k];
        }
        int vl=find(a,b,2*k+1,l,(l+r)/2);
        int vr=find(a,b,2*k+2,(l+r)/2,r);
        return min(vl,vr);
    }
};

void initial(void){
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
    cin >> N >> Q;
}
int main(void){
    initial();
    LazySegmentTree G(vector<int>(N,INF));
    for(int j=0;j<Q;j=j+1){
        int query;
        cin >> query;
        if(query==0){
            int s,t,x;
            cin >> s >> t >> x;
            G.update(s,t+1,x);
        }else{
            int s,t;
            cin >> s >> t;
            cout << G.find(s,t+1) << endl;
        }
    }
    return 0;
}
