#include <bits/stdc++.h>
using namespace std;

// recusive solution (top-down)
int lcs(string a, string b){
    if(a.empty() || b.empty()) return 0;

    if(a[a.length()-1]==b[b.length()-1]){
        return 1+lcs(a.substr(0,a.length()-1), b.substr(0,b.length()-1));
    }

    return max(lcs(a.substr(0,a.length()-1), b), lcs(a,b.substr(0,b.length()-1) ));
}

int main(){
    string a, b;
    int i,j;
    cin>>a;
    cin>>b;
    int c = 0;
    // c = lcs(a,b);
    
    //bottom-up approach.
    int arr[b.length()+1][a.length()+1];
    for(i=0;i<b.length()+1;i++){
        arr[i][0] = 0;
    }
    for(i=0;i<a.length()+1;i++){
        arr[0][i] = 0;
    }

    for(i=1;i<b.length()+1;i++){
        for(j=1;j<a.length()+1;j++){
            if(a.at(j-1)==b.at(i-1)){
                arr[i][j] = 1+arr[i-1][j-1];
            }else {
                arr[i][j] = max(arr[i-1][j], arr[i][j-1]);
            }
        }
    }

    c = arr[b.length()][a.length()];

    cout<<c;
}