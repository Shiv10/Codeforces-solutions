#include <bits/stdc++.h>
using namespace std;

int main(){
    int n, i,st,en;
    cin>>n;
    st=-1;
    en = n;
    bool flag = true;
    int a[n];
    for(i=0;i<n;i++){
        cin>>a[i];
    }
    for(i=0;i<n-1;i++){
        if(flag){
            if(a[i]>a[i+1]){
                st = i;
                flag=false;
            }
        }else {
            if(a[i]<a[i+1]){
                en = i+1;
                break;
            }
        }
    }

    reverse(a+st, a+en);
    bool f = true;
    for(i=0;i<n-1;i++){
        if(!(a[i]<=a[i+1])){
            f = false;
            break;
        }
    }

    if(st!=-1){
        if(f){
            cout<<"yes\n";
            cout<<st+1<<" "<<en<<endl; 
        }else {
            cout<<"no\n";
        }
    } else {
        cout<<"yes\n1 1";
    }
    return 0;
}