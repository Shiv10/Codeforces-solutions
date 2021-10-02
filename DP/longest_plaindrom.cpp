#include <bits/stdc++.h>
using namespace std;

int main(){
    string s;
    cin>>s;
    int i,j,n=s.length();
    int arr[n][n];
    for(i=0;i<n;i++){
        arr[i][i]=1;
    }
    for(int d = 0;d<=n; d++){
        for(i=0;i<n-d;i++){
            j = d+i-1;
            if(s[i]==s[j]&& d==2) arr[i][j] = 2;
            else if (s[i]==s[j]) arr[i][j]= arr[i+1][j-1]+2;
            else arr[i][j] = max(arr[i][j-1], arr[i+1][j]);
        }
    }
}