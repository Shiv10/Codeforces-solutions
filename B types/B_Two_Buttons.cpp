#include <bits/stdc++.h>
using namespace std;

int main(){
    int n,m;
    cin>>n>>m;
    int c=0;
    while(m>n){
        if(m%2==0){
            m=m/2;
        }else {
            m = m+1;
        }
        c++;
    }
    c+=n-m;
    cout<<c;
    return 0;
}