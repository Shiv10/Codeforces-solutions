#include <bits/stdc++.h>
using namespace std;

int main(){
    int n, i;
    string a;
    bool f = false;
    cin>>n;
    vector<string> v;

    for(i=0;i<n;i++){
        string b = "";
        cin>>b;
        if(f){
            v.push_back(b);
            continue;
        }
        if(b[0]=='O' && b[1]=='O'){
            b[0]='+';
            b[1]='+';
            f = true;
        }
        if(!f){
            if(b[3]=='O' && b[4]=='O'){
                b[3]='+';
                b[4]='+';
                f = true;
            }
        }
        v.push_back(b);
    }

    if(!f){
        cout<<"No";
        return 0;
    }
    cout<<"YES\n";
    for(auto x: v){
        cout<<x<<endl;
    }
    return 0;
}