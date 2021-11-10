#include <bits/stdc++.h>
using namespace std;

int main(){
    int n, a, i, one = 0;
    cin>>n;
    vector<int> v;
    vector<int> b;
    for(i=0;i<n;i++){
        cin>>a;
        if(a==1){
            one++;
        }
        v.push_back(a);
    }

    int ans = 0, sum = 0;

    for(i=0;i<n;i++){
        if (v[i]==0) sum++;
        else sum--;
        ans = max(ans,sum);
        if(sum<0){
            sum = 0;
        }
    }
    if(one==n){
        cout<<n-1;
    }else {
        cout<<one+ans;
    }
    return 0;

}