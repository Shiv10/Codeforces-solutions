#include <bits/stdc++.h>
using namespace std;



int main(){
    long long n,m,i,k;
    cin>>n>>m;
    long long mi, ma;
    mi = ma = 0;
    if (n%m==0){
        k = n/m;
        mi = (k*(k-1)/2)*m;
    } else {
        long long t = n%m;
        long long temp = m - t;
        k = n/m;
        long long k1 = n/m+1;
        mi = ((k*(k-1)/2)*temp)+((k1*(k1-1)/2)*t);
    }
    k = n-m+1;
    ma = k*(k-1)/2;
    cout<<mi<<" "<<ma;
    return 0;
}