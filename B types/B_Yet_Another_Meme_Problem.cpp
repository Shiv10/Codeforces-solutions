#include <bits/stdc++.h>
using namespace std;

int main() {
    int t;
    cin>>t;
    while(t>0){
        int a;
        int b;
        cin>>a>>b;
        cout<<(a*(to_string(b+1).length()-1))<<endl;
        t--;
    }
    
}