#include <bits/stdc++.h>
using namespace std;


int main(){
    int t;
    cin>>t;
    while(t-->0){
        int a, b, c;
        cin>>a>>b>>c;
        int n;
        n = abs(a-b)*2;
        if(a>n || b>n || c>n){
            cout<<-1<<endl;
            continue;
        }
        int out;
        out = c+abs(a-b)>n?c-abs(a-b):c+abs(a-b);
        cout<<out<<endl;
    }
}