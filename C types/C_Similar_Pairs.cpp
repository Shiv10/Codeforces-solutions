#include <bits/stdc++.h>
using namespace std;

int main(){
    int t;
    cin>>t;
    while(t-->0){
        int n;
        cin>>n;
        vector<int> even;
        vector<int> odd;
        int i,j,ev=0,od=0;
        for(i=0;i<n;i++){
            int temp;
            cin>>temp;
            if(temp%2==0){
                ev++;
                even.push_back(temp);
            }
            else{
                od++;
                odd.push_back(temp);
            }
        }

        if(ev%2==0 && od%2==0){
            cout<<"yes\n";
            continue;
        }
        int fl = 0;
        for(auto x: even){
            for(auto y: odd){
                if (abs(x-y)==1){
                    fl=1;
                    break;
                }
            }
            if(fl==1) break;
        }
        if(fl==1) cout<<"yes\n";
        else cout<<"no\n";
    }
}