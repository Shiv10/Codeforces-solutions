#include <bits/stdc++.h>
using namespace std;

int main() {
    int t;
    cin>>t;
    while(t-->0){
        int n;
        cin>>n;
        if(n==1){
            cout<<1<<endl;
            continue;
        }
        if (n%2==0){
            for(int i=2;i<=n;i+=2){
                cout<<i<<" "<<i-1<<" ";
            }
        } else if (n==3) {
            cout<<"3 1 2 ";
        } else {
            cout<<"3 1 2 ";
            for(int i=5;i<=n;i+=2){
                cout<<i<<" "<<i-1<<" ";
            }
        }
        cout<<endl;
    }
}