#include <bits/stdc++.h>
using namespace std;

#define N 300000
#define M 300000

int main(void){
	int n,m,idx,ans=0;
	int r[M+1],c[M+1];
	int rplace[N+1]={},cplace[N+1]={};

	cin>>n>>m;
	for(int i=1;i<=m;i++){
		cin>>r[i]>>c[i];
		if(rplace[r[i]]>0){
			idx=rplace[r[i]];
			rplace[r[idx]]=0;
			cplace[c[idx]]=0;
			ans--;
		}
		if(cplace[c[i]]>0){
			idx=cplace[c[i]];
			rplace[r[idx]]=0;
			cplace[c[idx]]=0;
			ans--;
		}
		rplace[r[i]]=i;
		cplace[c[i]]=i;
		ans++;
	}
	
	cout<<ans<<endl;
	return 0;
}
