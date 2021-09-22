#include <bits/stdc++.h>
using namespace std;

int main(){
    int n, c=1;
    string arr[] = {"Sheldon", "Leonard", "Penny", "Rajesh", "Howard"};
    cin>>n;
    while(c*5<n){
        n -= 5*c;
        c*=2;
    }
    cout<<arr[(n-1)/c];
    return 0;
}