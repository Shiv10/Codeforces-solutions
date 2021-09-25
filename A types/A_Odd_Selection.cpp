#include <bits/stdc++.h>
using namespace std;

int main(){
    int t;
    cin>>t;
    while(t-->0){
        int flag =0;
        int n,x, ev=0, od=0;
        cin>>n>>x;
        int a[n];
        for(int i=0;i<n;i++){
            cin>>a[i];
            if(a[i]%2==0) ev++;
            else od++;
        }
        for(int i=1;i<=od && i<=x;i+=2){
            int need = x-i;
            if(need<=ev){
                flag = 1;
            }
        }
        if (flag){
            cout<<"yes\n";
        }else {
            cout<<"No\n";
        }
    }
}