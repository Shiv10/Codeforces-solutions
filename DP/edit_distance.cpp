#include <bits/stdc++.h>
using namespace std;

int main(){
    string a,b;
    cin>>a>>b;
    int n,m,i,j,c=0;
    n = a.length();
    m = b.length();

    int arr[m+1][n+1];
    for(i=0;i<n+1;i++){
        arr[0][i] = i;
        arr[i][0] = i;
    }

    for(i=1;i<m+1;i++){
        for(j=1;j<n+1;j++){
            if(a[j-1]==b[i-1]){
                arr[i][j] = arr[i-1][j-1];
            }else {
                arr[i][j] = min(min(arr[i-1][j-1], arr[i-1][j]), arr[i][j-1])+1;
            }
        }
    }

    cout<<arr[m][n];
    return 0;
}