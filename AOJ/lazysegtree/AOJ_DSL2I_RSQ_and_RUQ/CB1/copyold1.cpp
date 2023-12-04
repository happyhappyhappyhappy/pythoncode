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
    using FP=function<M(M,int)>;
    int n;
    FX fx;
    FX fa;
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
                                int x = 1;
                                while(x < n_){
                                    x = x*2;
                                }
                                n = x;
                            }
    // 2023-12-02 19:35:02
    // ここから乃至もう一回コピー
};
