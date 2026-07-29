#include <bits/stdc++.h>
using namespace std;

#define N 300000
#define M 300000

int main(void){
	int n,m,ans=0;
	int r[M],c[M];
	bool rused[N+1]={},cused[N+1]={};

	cin>>n>>m;
	for(int i=0;i<m;i++){
		cin>>r[i]>>c[i];
	}
	for(int i=m-1;i>=0;i--){
		if((!rused[r[i]])&&(!cused[c[i]]))ans++;
		rused[r[i]]=true;
		cused[c[i]]=true;
	}
	cout<<ans<<endl;
	return 0;
}
