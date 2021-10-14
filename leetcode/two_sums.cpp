#include <bits/stdc++.h>
using namespace std;
vector<int> twoSum(vector<int> &nums, int target)
{
    int i, j;
    vector<int> sum;
    for (i = 0; i < nums.size(); i++)
    {
        vector<int> sums;
        for (j = i + 1; j < nums.size(); j++)
        {
            if (nums[i] + nums[j] == target)
            {
                sums.push_back(i);
                sums.push_back(j);
                return sums;
            }
        }
    }
    return sum;
}