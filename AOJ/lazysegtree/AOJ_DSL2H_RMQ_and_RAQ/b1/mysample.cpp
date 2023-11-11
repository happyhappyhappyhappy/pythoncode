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
template <typename T>
struct RMQ{
    const T INF = numeric_limits<T>::max();
    int n;
    vector<T> dat,lazy;
    RMQ(int n_):n(),dat(n_ *4,INF),lazy(n_ *4,0){
        int x = 1;
        while(x < n_){
            x = x*2;
        }
        n = x;
    }
    void set(int j,T x){
        dat[(n-1)+j]=x;
    }
    void build(){
        for(int k=n-2;k> -1;k=k-1){
            dat[k]=min(dat[k*2+1],dat[k*2+2]);
        }
    }
    void eval(int k){
        if(lazy[k] == 0)return;
        if(k < n-1){
            lazy[k*2+1]=lazy[k*2+1]+lazy[k];
            lazy[k*2+2]=lazy[k*2+2]+lazy[k];
        }
        dat[k]=dat[k]+lazy[k];
        lazy[k]=0;
    }
    void add(int a,int b,T x,int k,int l,int r){
        eval(k);
        if(a <= l && r <= b){
            lazy[k]=lazy[k]+x;
            eval(k);
        }else if(a < r && l < b){
            add(a,b,x,k*2+1,l,(l+r)/2);
            add(a,b,x,k*2+2,(l+r)/2,r);
            dat[k]=min(dat[k*2+1],dat[k*2+2]);
        }
    }
    void add(int a,int b,T x){
        add(a,b,x,0,0,n);
    }
    T query_sub(int a,int b,int k,int l,int r){
        eval(k);
        if ( r <= a || b <= l){
            return INF;
        }else if(a <= l && r <= b){
            return dat[k];
        }else{
            T vl=query_sub(a,b,k*2+1,l,(l+r)/2);
            T vr=query_sub(a,b,k*2+2,(l+r)/2,r);
            return min(vl,vr);
        }
    }
    T query(int a,int b){
        return query_sub(a,b,0,0,n);
    }
    // 二部探索処理は利用しないので省略
    inline T operator[](int a){
        return query(a,a+1);
    }
    void print(){
        for(int j=0;j<n;j=j+1){
            cout << (*this)[j];
            if(j!=n)cout << ",";
        }
        cout << "\n" << flush;
    }
};
void initial(void){
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
}
int main(void){
    initial();
    int N,Q;
    cin >> N >> Q;
    RMQ<int> rmq(N);
    for(int j=0;j<N;j=j+1){
        rmq.set(j,0);
    }
    rmq.build();
    vector<int> ans;
    for(int j=0;j<Q;j=j+1){
        int c;
        cin >> c;
        if(c == 0){
            int s,t,x;
            cin >> s >> t >> x;
            rmq.add(s,t+1,x);
        }else if(c == 1){
            int s,t;
            cin >> s >> t;
            int val;
            // rmq.print();
            val=rmq.query(s,t+1);
            ans.push_back(val);
        }
    }
    for(auto j:ans){
        cout << j << "\n" << flush;
    }
    return 0;
}
