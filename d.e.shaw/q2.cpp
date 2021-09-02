#include <bits/stdc++.h>
using namespace std;

int findIndex(vector<int> arr, int k){
    int n = arr.size();
    int start = 0, end = n-1;

    while(start<=end){
        int mid = (start+end)/2;
        if(arr[mid]) return mid+1;

        else if(arr[mid]<k) start = mid+1;

        else end=mid-1;
    }

    return end+1;
}

vector<int> findKthTask(vector<int> tasks, vector<int> k){
    vector<int> v, res;
    int c = 0;
    for(auto x: k){
        if (c==0){
            v.push_back(tasks[c]);
        }else {
            int index = findIndex(v, tasks[c]);
            v.insert(v.begin()+index, tasks[c]);
        }
        c++;
        res.push_back(v[x-1]);
    }
    return res;
}