#include <bits/stdc++.h>
using namespace std;


unordered_map<int, vector<int>> memo;
vector<int> minSum(int n, vector<int> squares ){
    
    if(memo.find(n)!=memo.end()){
        return memo[n];
    }

    if (n==0){
        return vector<int>();
    }

    if(n<0){
        vector<int> vec;
        vec.push_back(-1);
        return vec;
    }

    vector<int> result(10000);
    for(auto x: squares){
        vector<int> res;
        res = minSum(n-x, squares);
        if(res.size()==0){
            res.push_back(x);
            if(res.size()<result.size()){
                result = res;
            }
        }else {
            if(res[0]!=-1){
                res.push_back(x);
                if(res.size()<result.size()){
                    result = res;
                }
            }
        }
    }

    memo [n] = result;
    return result;
}

int numSquares(int n)
{
    vector<int> squares;
    int i, j;
    for (i = 1; i < n; i += 1)
    {
        if (i * i <= n)
        {
            squares.push_back(i * i);
            continue;
        }
        break;
    }
    
    vector<int> result = minSum(n, squares);
    for(auto x: result){
        cout<<x<<" ";
    }

    return 0;
}


int main(){
    int i;
    cin>>i;
    int n = numSquares(i);
    return 0;
}