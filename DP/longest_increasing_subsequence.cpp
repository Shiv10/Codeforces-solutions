#include <bits/stdc++.h>
using namespace std;

int main(){
    int n,i,j,m=1;
    cin>>n;
    int a[n];
    int sol[n];
    for(i=0;i<n;i++){
        cin>>a[i];
        sol[i] = 1;
    }
    
    for(i=1;i<n;i++){
        for(j=0;j<i;j++){
            if(a[i]>=a[j]){
                if(sol[i]<sol[j]+1){
                    sol[i] = sol[j]+1;
                }
            }
        }
    }

    for(i=0;i<n;i++){
        if(m<sol[i]) m=sol[i];
    }

    cout<<m;
}