#include <bits/stdc++.h>
using namespace std;

int main(){
    int t;
    cin>>t;
    while(t>0){
        int n, i, s= 0;
        cin>>n;
        int arr[n];
        for(i=0;i<n;i++){
            cin>>arr[i];
            s+=arr[i];
        }
        if(s%n!=0){
            cout<<-1<<endl;
            t--;
            continue;
        }

        int avg = s/n;
        int count = 0;
        for(i=0;i<n;i++){
            if(arr[i]>avg) count++;
        }
        cout<<count<<endl;
        t--;
    }
    return 0;
}