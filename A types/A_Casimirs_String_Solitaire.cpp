#include <bits/stdc++.h>
using namespace std;

int main(){
    int t;
    cin>>t;
    while(t-->0){
        int a,b,c;
        a=b=c=0;
        string s;
        cin>>s;
        for(int i =0;i<s.length();i++){
            if(s[i]=='A') a++;
            if(s[i]=='B') b++;
            if(s[i]=='C') c++;
        }
        if(a+c==b) cout<<"YES\n";
        else cout<<"NO\n";
    }
}