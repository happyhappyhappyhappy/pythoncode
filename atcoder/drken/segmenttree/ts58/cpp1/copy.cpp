#include<bits/stdc++.h>
using namespace std;

template<class Monoid,Monoid(*OP)(Monoid,Monoid),Monoid IDENTITY> struct SegTree {
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
        do {
            while(l % 2 == 0) l >>=1;
            if(!f(OP(sum,dat[l]))){
                while(l < offset){
                    l = l * 2;
                    if ( f(OP(sum,dat[l]))){
                        sum = OP(sum,dat[l]);
                        ++l;
                    }
                }
                return l - offset;
            }
            sum = OP(sum,dat[l]);
            ++l;
        }while ((l & -l) != l);
        return N;
    }
    int min_left(const function<bool(Monoid)> f,int r = -1){
        if ( r == 0)return 0;
        if ( r == -1) r = N;
        r += offset;
        Monoid sum = IDENTITY;
        do {
            --r;
            while ( r > 1 && (r % 2)) r >>= 1;
            if (!f(OP(dat[r],sum))){
                while(r < offset){
                    r = r * 2+1;
                    if ( f(OP(dat[r],sum))){
                        sum = OP(dat[r],sum);
                        --r ;
                    }
                }
                return r+1 - offset;
            }
            sum = OP(dat[r],sum);
        }while (( r & -r) != r);
        return 0;
    }
    friend ostream& operator << (ostream &s,const SegTree &seg){
        for ( int j = 0;j < seg.size(); ++j){
            s << seg[j];
            if ( j != seg.size()-1) s << " ";
        }
        return s;
    }
};

const int INF = 1<<30;

int op(int a,int b){
    return max(a,b);
}

int main(void){
    int N,Q;
    cin >> N >> Q;
    SegTree<int,op,-INF> seg(N);
    for(int j=0;j<N;++j){
        seg.set(j,0);
    }
    while(Q--){
        int t;
        cin >> t;
        if(t == 1){
            int pos,x;
            cin >> pos >> x;
            --pos;
            cout << seg << "\n" << flush;
            seg.set(pos,x);
            cout << seg << "\n" << flush;
        }else{
            int l,r ;
            cin >> l >> r;
            --l;
            --r;
            cout << seg.prod(l,r) << endl;
        }
    }
}
