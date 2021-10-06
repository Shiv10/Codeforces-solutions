#include <bits/stdc++.h>
using namespace std;

int main(){
    int t;
    cin>>t;
    while(t-->0){
        int n,m;
        cin>>n>>m;
        vector<int> a(n);
        vector<int> b(m);
        int i,j;
        bool flag=false;
        int temp;
        for(i=0;i<n;i++){
            cin>>temp;
            a.push_back(temp);
        }

        for(i=0;i<m;i++){
            cin>>temp;
            if(!flag){
                if(find(a.begin(), a.end(), temp)!=a.end()){
                    j=temp;
                    flag = true;
                }
            }
        }

        if(flag){
            cout<<"YES\n";
            cout<<1<<" "<<j<<endl;
            continue;
        }
        cout<<"NO\n";
    }
}