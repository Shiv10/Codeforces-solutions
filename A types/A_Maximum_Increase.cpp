#include <bits/stdc++.h>
using namespace std;

int main(){
    int n, i, max = 0, cur = 0;
    vector<int> v;
    cin>>n;
    for(i=0;i<n;i++){
        int a;
        cin>>a;
        v.push_back(a);
    }

    cur = 1;
    max = 1;
    for(i=0;i<n-1;i++){
        if(v[i+1]>v[i]){
            cur++;
        }else {
            if(cur>max){
                max=cur;
            }
            cur=1;
        }
    }
    if (cur>max){
        max= cur;
    }
    cout<<max;
    return 0;
}