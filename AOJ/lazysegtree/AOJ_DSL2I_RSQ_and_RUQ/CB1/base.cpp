#include<bits/stdc++.h>
#ifdef LOCAL
#include"/wrk/debug/debug.h"
#include"/wrk/debug/t_debug.h"
// #include"/wrk/sakura-cpp/lib/dump.hpp"
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
template<typename X,typename M>
struct SegTreeLazyProportional{
    using FX=function<X(X,X)>;
    using FA=function<X(X,M)>;
    using FM=function<M(M,M)>;
    using FP = function<M(M,int)>;
    int n;
    FX fx;
    FA fa;
    FM fm;
    FP fp;
    const X ex;
    const M em;
    vector<X> dat;
    vector<M> lazy;
    SegTreeLazyProportional(int n_,
                            FX fx_,FA fa_,FM fm_,FP fp_,
                            X ex_,M em_)
                            : n(),fx(fx_),fa(fa_),fm(fm_),fp(fp_),
                            ex(ex_),em(em_),
                            dat(n_*4,ex),lazy(n_*4,em){
                                int x=1;
                                while(x < n_){
                                    x = x * 2;
                                }
                                n = x;
                            }
    void set(int j,X x){
        dat[(n-1)+j]=x;
    }
    void build(){
        for(int k=n-2;0<=k;k=k-1){
            dat[k]=fx(dat[k*2+1],dat[k*2+2]);
        }
    }
    void eval(int k,int len){
        if(lazy[k]==em){
            return;
        }
        if(k < n-1){
            lazy[k*2+1]=fm(lazy[k*2+1],lazy[k]);
            lazy[k*2+2]=fm(lazy[k*2+2],lazy[k]);
        }
        dat[k]=fa(dat[k],fp(lazy[k],len));
        lazy[k]=em;
    }
    void update(int a,int b,M x,int k,int l,int r){
        eval(k,r-l);
        if(a <= l && r <= b){
            lazy[k]=fm(lazy[k],x);
            eval(k,r-l);
        }else if(a < r && l < b){
            int mid=(l+r)>>1;
            update(a,b,x,k*2+1,l,mid);
            update(a,b,x,k*2+2,mid,r);
            dat[k]=fx(dat[k*2+1],dat[k*2+2]);
        }
    }
    void update(int a,int b,M x){
        update(a,b,x,0,0,n);
    }
    X getSum_sub(int a,int b,int k,int l,int r){
        eval(k,r-l);
        if(r <= a || b <= l){
            return ex;
        }else if(a <= l && r <= b){
            return dat[k];
        }else{
            int mid=(l+r)>>1;
            X vl=getSum_sub(a,b,2*k+1,l,mid);
            X vr=getSum_sub(a,b,k*2+2,mid,r);
            return fx(vl,vr);
        }
    }
    X getSum(int a,int b){
        return getSum_sub(a,b,0,0,n);
    }
    inline X operator[](int a){
        return getSum(a,a+1);
    }
    void print(){
        for(int j=0;j<n;j=j+1){
            cout << (*this)[j];
            if(j != n-1){
                cout << ",";
            }
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
    int n,q;
    cin >> n >> q;
    using X = long long;
    using M = long long;
    auto fx = [](X x1,X x2)->X{return x1+x2;};
    auto fa = [](X x,M m)->X{return m;};
    auto fm = [](M m1,M m2)->M{return m2;};
    auto fp = [](M m,long long n)->M{return m*n;};
    long long ex = 0;
    long long em = numeric_limits<int>::max();
    SegTreeLazyProportional<X,M> rsq(n,fx,fa,fm,fp,ex,em);
    vector<long long> ans;
    for(int j=0;j<q;j=j+1){
        int c;
        cin >> c;
        if(c==0){
            int s,t;
            long long val;
            cin >> s >> t >> val;
            rsq.update(s,t+1,val);
            // rsq.print();
        }else if(c==1){
            int s,t;
            cin >> s >> t;
            // rsq.print();
            long long x;
            x = rsq.getSum(s,t+1);
            ans.push_back(x);
        }
    }
    for(int j=0;j<(int)ans.size();j=j+1){
        cout << ans[j] << "\n" << flush;
    }
    return 0;
}
