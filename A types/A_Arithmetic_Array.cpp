#include <bits/stdc++.h>
using namespace std;

int main(){
    int t;
    cin>>t;
    while(t>0){
        int n;
        cin>>n;
        int arr[n];
        int i,s=0;
        for(i=0;i<n;i++){
            cin>>arr[i];
            s += arr[i];
        }
        if (s==n){
            cout<<0<<endl;
            t--;
            continue;
        }else if(s<n){
            cout<<1<<endl;
            t--;
            continue;
        }
        cout<<s-n<<endl;
        t--;
    }
    return 0;
}