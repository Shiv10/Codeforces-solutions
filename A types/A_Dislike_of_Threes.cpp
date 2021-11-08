#include <bits/stdc++.h>
using namespace std;

int main(){
    int m = 0, c=0;
    vector<int> input;
    vector<int> series;
    int n,i,a;
    cin>>n;
    for(i=0;i<n;i++){
        cin>>a;
        if(m<a){
            m = a;
        }
        input.push_back(a);
    }
    int k = 1;
    while(c<=m){
        if(k%10==3 || k%3==0){
            k++;
            continue;
        }
        series.push_back(k);
        k++;
        c++;
    }

    for(i=0;i<input.size();i++){
        cout<<series[input[i]-1]<<endl;
    }
    return 0;
}