#include <bits/stdc++.h>
using namespace std;

int main(){
    int n, m, k, i, c=0, count = 0;
    cin>>n>>m>>k;
    vector<int> vec;
    for(i=0;i<m+1;i++){
        int a;
        cin>>a;
        vec.push_back(a);
    }

    vector<vector<int>> bin;
    for(i=0;i<vec.size();i++){
        int a = vec[i];
        vector<int> ans;
        while(a>0){
            ans.push_back(a%2);
            a = a/2;
        }
        bin.push_back(ans);
    }

    for (i=0;i<bin.size()-1;i++){
        int p;
        c = 0;
        if (bin[i].size()<bin[m].size()){            
            p = bin[i].size();
            for(int j=p;j<bin[m].size();j++){
                if (bin[m][j]==1){
                    c++;
                }
            }
        } else {
            p = bin[m].size();
            for(int j =p; j<bin[i].size();j++){
                if (bin[i][j] == 1){
                    c++;
                }
            }
        }

        for (int j=0;j<p;j++){
            if (bin[i][j]!=bin[m][j]){
                c++;
            }
        }
        if (c<=k){
            count++;
        }
    }

    cout<<count;

    return 0;
    
}