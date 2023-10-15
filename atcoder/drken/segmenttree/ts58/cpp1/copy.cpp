#include<bits/stdc++.h>
using namespace std;

template<class Monoid,Monoid(*op)(Monoid,Monoid),Monoid IDENTITY> struct SegTree {
    int N;
    int offset;
    vector<Monoid> dat;
    SegTree(){}
    SegTree(int n): N(n){
        init(n);
    }
    SegTree(const vector<Monoid> &v):N(v.size()){
        init(v);
    }
    void init(int n){
        N = n;
        offset = 1;
        while(offset < N)offset *= 2;
        dat.assign(offset*2,IDENTITY);
    }
    void init(const vector<Monoid> &v){
        N = (int)v.size();
        offset = 1;
        while(offset < N) offset *= 2;
        dat.assign(offset*2,IDENTITY);
        for(int j=0;j<N;++j) dat[j+offset]=v[j];
        build();
    }
    void build(){
        for(int k=offset-1;k>0;--k)dat[k]=OP(dat[k*2],dat[k*2+1]);
    }
    int size() const{
        return N;
    }
    Monoid operator [] (int a) const { return dat[a+offset];}
    void set(int a,const Monoid &v){
        int k=a+offset;
        dat[k]=v;
        while(k>>=1)dat[k]=OP(dat[k*2],dat[k*2+1]);
    }
    Monoid prod(int a,int b){
        Monoid vleft = IDENTITY,vright = IDENTITY;
        for(int left = a+offset,right=b+offset;left < right;
        left >>=1, right >>=1){
            if ( left & 1) vleft = OP(vleft,dat[left++]);
            if(right & 1) vright=OP(dat[--right],vright);

        }
        return OP(vleft,vright);
    }
    Monoid all_prod(){return dat[1];}
    int max_right(const function<bool(Monoid)> f,int l=0){
        if ( l == N) return N;
        l = l + offset;
        Monoid sum = IDENTITY;
    // TODO: L.69 から
    }

}
