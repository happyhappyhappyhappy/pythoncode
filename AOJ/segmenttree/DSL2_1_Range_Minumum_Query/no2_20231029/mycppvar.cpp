#include<bits/stdc++.h>
#ifdef LOCAL
#include"/wrk/cdebug/debug.h"
#include"/wrk/cdebug/t_debug.h"
#include"/wrk/cdebug/cpp-dump/dump.hpp"
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
int const INF = ((1<<31)-1);

struct SegmentTree{
    private:
        int n;
        vector<int> node;
    public:
        SegmentTree(vector<int> v){
            int sz = (int)v.size();
            n = 1;
            while ( n < sz){
                n=n*2;
            }
            node.resize(2*n-1,INF);
            for(int j=0;j<sz;j=j+1){
                node[(n-1)+j]=v[j];
            }
            for(int j=n-2;0 <= j ; j=j-1){
                node[j]=min(node[2*j+1],node[2*j+2]);
            }
        }
        void update(int x,int val){
            x = x + (n-1);
            node[x] = val;
            while(0 < x){
                x = (x -1)/2;
                node[x]=min(node[2*x+1],node[2*x+2]);
            }
        }
        int getmin(int a,int b,int k=0,int l=0,int r=-1){
            if(r < 0) {
                r = n;
            }
            if(r <= a || b <= l)
            {
                debug("NG.Pat0.a={%d} <= l = {%d} or  r = {%d} <= b = {%d}でした(現在ノード%d)\n",a,l,r,b,k);
                debug("この場合は 最大値というか単位元を返します\n");
                return INF;
            }
            if(a <= l && r <= b){
                debug("Pat1.a={%d} <= l = {%d} && r = {%d} <= b = {%d}です(現在ノード%d)\n",a,l,r,b,k);
                debug("この場合は node[%d] = %d で可能です\n",k,node[k]);
                return node[k];
            }
            debug("Pat2.a={%d} <= l = {%d} && r = {%d} <= b = {%d}です(現在ノード%d)\n",a,l,r,b,k);
            debug("この場合は node[%d]とnode[%d] につなげてそれぞれの下を取って最小値を見ます \n",2*k+1,2*k+2);

            int vl=getmin(a,b,2*k+1,l,(l+r)/2);
            int vr=getmin(a,b,2*k+2,(l+r)/2,r);
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
    SegmentTree seg(vector<int>(N,INF));
    for(int j=0;j<Q;j=j+1){
        int c,x,y;
        cin >> c >> x >> y;
        if(c == 0){
            seg.update(x,y);
        }else{
            int a=seg.getmin(x,y+1);
            cout << a << "\n" << flush;
        }
    }
    return 0;
}
