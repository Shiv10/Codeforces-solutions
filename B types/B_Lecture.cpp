#include <bits/stdc++.h>
using namespace std;
int main(){
    vector<string> lang;
    string a, b;
    int n, m, i;
    cin>>n>>m;
    for(i=0;i<m;i++){
        cin>>a>>b;
        lang.push_back(a);
        lang.push_back(b);
    }
    string temp;
    getline(cin, temp);
    string str;
    string s[n];
    getline(cin, str);
    str = str+' ';
    int l = str.length();
    a = "";
    int k = 0;
    for(i=0;i<l;i++){
        if (str[i]!=' '){
            a+=str[i];
        }
        else{
            s[k] = a;
            k++;
            a = "";
        }
    }
    string final;

    for (auto x: s){
        auto it = find(lang.begin(), lang.end(), x);
        int index = it - lang.begin();
        int ind;
        string word;
        if(index%2==0){
            ind=index+1;
            word = lang[index];
        } else{
            ind = index-1;
            word = lang[ind];
        }

        if (lang[index].length()<lang[ind].length()){
            word = lang[index];
        }

        if (lang[index].length()>lang[ind].length()){
            word = lang[ind];
        }

        final += word+' ';
    }

    cout<<final;
    

    return 0;
}