#include <bits/stdc++.h>
using namespace std;

int main(){
    int n,m, s, t;
    cin>>n>>m>>s>>t;
    int arr[n+1][m+1];
    memset(arr, -1, sizeof(arr));
    arr[s][t] = 0;
    cout<<s<<" "<<t<<endl;
    for(int i = 0;i<n*m;i++){
        if(s-1>0 && arr[s-1][t]!=0){
            s--;
            arr[s][t] = 0;
            cout<<s<<" "<<t<<endl;
            continue;
        }

        if(t-1>0 && arr[s][t-1]!=0){
            t--;
            arr[s][t] = 0;
            cout<<s<<" "<<t<<endl;
            continue;
        }

        if(s+1<=n && arr[s+1][t]!=0){
            s++;
            arr[s][t] = 0;
            cout<<s<<" "<<t<<endl;
            continue;
        }

        if(t+1<=m && arr[s][t+1]!=0){
            t++;
            arr[s][t] = 0;
            cout<<s<<" "<<t<<endl;
            continue;
        }

        bool f = true;
        for(int j = 1; j <= m; j++){
            if(arr[s][j]==-1){
                t = j;
                arr[s][t] = 0;
                cout<<s<<" "<<t<<endl;
                f = false;
                break;
            }
        }

        if (f){
            for(int j=1; j<=n; j++){
                if(arr[j][t]==-1){
                    s = j;
                    arr[s][t]=0;
                    cout<<s<<" "<<t<<endl;
                    break;
                }
            }
        }

    }
    return 0;
}