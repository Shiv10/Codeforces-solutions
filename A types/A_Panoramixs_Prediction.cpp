#include <bits/stdc++.h>
using namespace std;

bool isPrime(int n){
    int c = 0, i;
    for(i=1;i<n;i++){
        if(n%i==0) c++;
        
        if(c>1) break;
    }

    return c==1;
}

int main(){
    int x, y, i, c;
    cin>>x>>y;

    for(i = x+1; i<=y; i++){
        if(isPrime(i)){
            if(i==y){
                cout<<"YES";
                return 0;
            }
            break;
        }
    }
    cout<<"NO";
    return 0;
}