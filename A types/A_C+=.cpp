#include <bits/stdc++.h>
using namespace std;

int main(){
    int t, n, m, p;
    cin>>t;
    while(t>0){
        cin>>n>>m>>p;
        int s, c;
        s = 0;
        c = 0;
        while(s<=p){
            if (n<m){
                n += m;
                s = n;
            } else {
                m += n;
                s = m;
            }
            c++;
        }
        cout<<c<<endl;
        t--;
    }
}