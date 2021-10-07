#include <bits/stdc++.h>
using namespace std;

bool canConstruct(int n, vector<int> v){
    if(n==0){
        return true;
    }

    if(n<0){
        return false;
    }
    bool res = false;
    for(int i=0;i<v.size();i++){
        bool temp;
        temp = canConstruct(n-v[i],v);
        if(temp){
            return true;
        }
    }
    return res;
}



int main(){
    vector<int> v;
    v.push_back(1);
    v.push_back(2);
    v.push_back(3);
    v.push_back(4);
    int n=5,i,j;
    // cout<<canConstruct(5,v);

    int arr[n+1][v.size()];
    for(i=0;i<v.size();i++){
        arr[0][i] = 1;
    }

    for(i=1;i<n+1;i++){
        for(j=0;j<v.size();j++){
            int x,y=0;
            x = (i-v[j]>=0)? arr[i-v[j]][j]:0;

            if(j>=1){
                y  = arr[i][j-1];
            }

            arr[i][j]=x+y;
        }
    }

    cout<<arr[n][v.size()-1];
    return 1;
}