#include <bits/stdc++.h>
using namespace std;

int n, m;
map<int, vector<int>> d;
int cnt = 0;
int visited[10000000];

void dfs(int n, int *arr, int c){
    visited[n-1] = 1;

    if(arr[n-1]==1) c++;
    else c = 0;

    if(c>m) return;

    if(d[n].size()==1 && visited[d[n][0]-1]==1){
        if(c<=m && n!=1) cnt ++;

        return;
    }    

    for(auto i:d[n]){
        if(visited[i-1]==0){
            dfs(i,arr,c);
        }
    }
}

int main(){
    cin>>n>>m;
    memset(visited,0,sizeof(visited));
    int arr[n];
    for(int i=0;i<n;i++){
        cin>>arr[i];
    }

    for(int i=0;i<n-1;i++){
        int a,b;
        cin>>a>>b;
        if (d.find(a)==d.end()){
            vector<int> v;
            v.push_back(b);
            d[a] = v;
        }else {
            d[a].push_back(b);
        }

        if(d.find(b)==d.end()){
            vector<int> v1;
            v1.push_back(a);
            d[b] = v1;
        }else {
            d[b].push_back(a);
        }
    }

    dfs(1, arr, 0);
    cout<<cnt;
}