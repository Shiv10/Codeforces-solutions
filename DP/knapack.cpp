#include <bits/stdc++.h>
using namespace std;

int main(){
    int w, i, n, j;
    cin>>n;
    int weights[n];
    int val[n];
    for(i=0;i<n;i++){
        cin>>weights[i]>>val[i];
    }
    cin>>w;
    int arr[n+1][w+1];
    for(i=0;i<n+1;i++){
        arr[i][0] = 0;
    }

    for(i=0;i<w+1;i++){
        arr[0][i] = 0;
    }

    for(i=1;i<n+1;i++){
        for(j=1;j<w+1;j++){
            if(weights[i-1]<=w){
                arr[i][j] = max((val[i-1]+arr[i-1][w-weights[i-1]]), arr[i-1][j]);
            }else {
                arr[i][j] = arr[i-1][j];
            }
        }
    }

    cout<<arr[n][w];
    return 0;
}