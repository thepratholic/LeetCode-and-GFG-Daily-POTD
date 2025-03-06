#include<bits/stdc++.h>
using namespace std;

class Solution
{
public:
    vector<int> findMissingAndRepeatedValues(vector<vector<int>> &grid)
    {
        vector<int> ans;
        int repeat = 0, n = grid.size();

        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < n; j++)
            {
                ans.push_back(grid[i][j]);
            }
        }

        unordered_map<int, int> freq;
        for (int num : ans)
        {
            freq[num]++;
        }

        for (auto &p : freq)
        {
            if (p.second == 2)
            {
                repeat = p.first;
                break;
            }
        }

        int expectedSum = (n * n * (n * n + 1)) / 2;
        int actualSum = 0;
        for (int num : ans)
        {
            actualSum += num;
        }

        int missing = repeat + (expectedSum - actualSum);
        return {repeat, missing};
    }
};