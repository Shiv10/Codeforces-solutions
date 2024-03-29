
#include <bits/stdc++.h>
using namespace std;

void overlap(vector<pair<int, int> > v)
{

	int ans = 0;
	int count = 0;
	vector<pair<int, char> > data;

	for (int i = 0; i < v.size(); i++) {
		data.push_back({ v[i].first, 'x' });
		data.push_back({ v[i].second, 'y' });
	}

	sort(data.begin(), data.end());

    for(auto x: data){
        cout<<x.first<<" "<<x.second<<endl;
    }
	for (int i = 0; i < data.size(); i++) {
		if (data[i].second == 'x')
			count++;
		if (data[i].second == 'y')
			count--;
		ans = max(ans, count);
	}
	cout << ans << endl;
}

int main()
{
	vector<pair<int, int> > v
		= { { 1, 2 }, { 2, 4 }, { 3, 6 } };
	overlap(v);
	return 0;
}
