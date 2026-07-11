#include<bits/stdc++.h>

using namespace std;
using pi=pair<int,int>;

int main(){
  int n,m;
  cin >> n >> m;
  int kind=0;
  vector<int> cnt(n+1);
  vector<vector<pi>> change(m+1);
  for(int i=0;i<n;i++){
    int a,b,d;
    cin >> a >> d >> b;
    if(cnt[a]==0){kind++;}
    cnt[a]++;
    change[d].push_back({a,b});
  }
  for(int i=1;i<=m;i++){
    for(auto &nx : change[i]){
      cnt[nx.first]--;
      if(cnt[nx.first]==0){kind--;}
      if(cnt[nx.second]==0){kind++;}
      cnt[nx.second]++;
    }
    cout << kind << "\n";
  }
  return 0;
}
