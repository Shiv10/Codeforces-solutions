#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
    vector<string> generateParenthesis(int n) {
        vector<string> v;
        v = generate(n, "");
        return v;
    }
    
    vector<string> generate(int n, string s){
        int r = 0, l = 0;
        for(auto x: s){
            if(x=='(') l++;
            else r++;
        }
        
        vector<string> v;
        
        if(l==n && r==n){
            v.push_back(s);
            return v;
        }
        
        if(l>r && l<n){
            vector<string> temp;
            string temp_s = s;
            temp_s += ")";
            temp = generate(n, temp_s);
            for(auto x: temp){
                v.push_back(x);
            }
            
            s += "(";
            temp = generate(n, s);
            for(auto x: temp){
                v.push_back(x);
            }
        }else if(l==r){
            vector<string> temp;
            string temp_s = s;
            temp_s += "(";
            temp = generate(n, temp_s);
            for(auto x: temp){
                v.push_back(x);
            }
        } else if(l>r && l==n){
            vector<string> temp;
            string temp_s = s;
            temp_s += ")";
            temp = generate(n, temp_s);
            for(auto x: temp){
                v.push_back(x);
            }
        }
        return v;
    }
};