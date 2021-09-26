#include <bits/stdc++.h>
using namespace std;

int main(){
    int t;
    cin>>t;
    while(t-->0){
        int n;
        cin>>n;
        int arr[n];
        int i, first=-1, last=-1;
        for(i=0;i<n;i++){
            cin>>arr[i];
        }
        for(i=0;i<n;i++){
            if(arr[i]==1){
                last =i;
            }
            if(first==-1 && arr[i]==1){
                first = i;
            }
        }
        int count = 0;
        for(i=first;i<=last;i++){
            if(arr[i]==0){
                count++;
            }
        }
        cout<<count<<endl;
    }
}