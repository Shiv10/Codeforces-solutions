#include <bits/stdc++.h>
using namespace std;

int main(){
    int n, i;
    cin>>n;
    if(n%2!=0) {
        cout<<-1;
        return 0;
    }

    int arr[n];
    for(i=2;i<=n;i+=2){
        arr[i-2]=i;
        arr[i-1]=i-1;
    }

    for(i=0;i<n;i++){
        cout<<arr[i]<<" ";
    }
    return 0;
}