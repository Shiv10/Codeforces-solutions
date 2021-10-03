#include <bits/stdc++.h>
using namespace std;

int main(){
    int n, i, j;
    cin>>n;
    int a[n];
    int lis[n];
    int lds[n];
    for(i=0;i<n;i++){
        cin>>a[i];
        lis[i]=0;
        lds[i]=0;
    }

    for(i=1;i<n;i++){
        for(j=0;j<i;j++){
            if(a[i]>a[j]){
                if(lis[i]<lis[j]+1){
                    lis[i]=lis[j]+1;
                }
            }
        }
    }

    for(i=n-2;i>-1;i--){
        for(j=n-1;j>i;j--){
            if(a[i]>a[j] && lds[i]<lds[j]+1){
                lds[i]=lds[j]+1;
            }
        }
    }
    int m = 0;
    for(i=0;i<n;i++){
        if (lis[i]+lds[i]-1>m){
            m = lis[i]+lds[i]-1;
        }
    }
    cout<<m;
}