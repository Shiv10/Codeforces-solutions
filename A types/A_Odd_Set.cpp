#include <bits/stdc++.h>
using namespace std;

int main(){
    int t;
    cin>>t;
    while(t>0){
        int n, i, ev = 0, od = 0;
        cin>>n;
        for(i=0;i<n*2;i++){
            int a;
            cin>>a;
            if(a%2==0){
                ev++;
            }else{
                od++;
            }
        }

        if (ev==od){
            cout<<"Yes\n";
        }else {
            cout<<"No\n";
        }
        t--;
    }
    return 0;
}