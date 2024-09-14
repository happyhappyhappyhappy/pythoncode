#include <bits/stdc++.h>
using namespace std;

int main() {
	string s, t;
	cin >> s >> t;
	vector<string> ans;
	int n = s.size();
	while (s != t) {
		string nxt(n, 'z');
		for (int i = 0; i < n; i++) {
			if (s[i] != t[i]) {
				string tmp = s;
				tmp[i] = t[i];
				nxt = min(nxt, tmp);
			}
		}
		ans.push_back(nxt);
		s = nxt;
	}
	int sz = ans.size();
	cout << sz << '\n';
	for (string e : ans) cout << e << '\n';
}
