#include <bits/stdc++.h>
using namespace std;

int main(){
    long long int t;
    cin>>t;
    while(t>0){
        long long int n, m, x;
        cin>>n>>m>>x;
        int i,j;
        j = (x%n==0?(x/n)-1:x/n);
        i = x%n==0?(n-1):(x - 1 - (n*(x/n)));
        cout<<(m*i)+j+1<<endl;
        t--;
    }
    return 0;
}
