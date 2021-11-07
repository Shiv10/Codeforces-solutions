#include <bits/stdc++.h>
using namespace std;

int main(){
    int n,m, i,a;
    cin>>n;
    vector<int> boys;
    for(i=0;i<n;i++){
        cin>>a;
        boys.push_back(a);
    }

    cin>>m;
    vector<int> girls;
    for(i=0;i<m;i++){
        cin>>a;
        girls.push_back(a);
    }

    sort(boys.begin(), boys.end());
    sort(girls.begin(), girls.end());

    int l , r, c;
    l = r = c = 0;

    while(l<n && r<m){
        if(abs(boys[l]-girls[r])<=1){
            l++;
            r++;
            c++;
        }else {
            if(boys[l]<girls[r]){
                l++;
            }else {
                r++;
            }
        }
    }

    cout<<c;


}