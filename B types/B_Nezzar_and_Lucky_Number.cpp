#include <bits/stdc++.h>
using namespace std;

int main(){
    int t;
    cin>>t;
    while(t>0){
        int q, d;
        cin>>q>>d;
        for(int i=0;i<q;i++){
            int n;
            cin>>n;
            if(n>d*10){
                cout<<"YES\n";
                continue;
            }
            int flag = 0;
            while(n>=d){
                if(n%d==0){
                    flag = 1;
                    break;
                }
                n-=10;
            }
            if (flag){
                cout<<"YES\n";
            }else {
                cout<<"NO\n";
            }
        }
        t--;
    }
}