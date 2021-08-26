#include <bits/stdc++.h>
using namespace std;

int main(){
    int t;
    cin>>t;
    while(t--){
        int n, i, c = 0;
        cin>>n;
        vector<int> v;
        for(i = 0; i<n;i++){
            int a;
            cin>>a;
            v.push_back(a);
        }

        for(i=0;i<n-1;i++){
            int a,b;
            a = min(v[i], v[i+1]);
            b = max(v[i],v[i+1]);
            if(b<=a*2) continue;
            else {
                while(a*2<b){
                    c++;
                    a*=2;
                }
            }
        }
        cout<<c<<endl;
    }
}