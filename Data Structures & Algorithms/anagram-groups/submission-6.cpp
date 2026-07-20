#include <iostream>
#include <algorithm> // for std::sort
#include <string>
#include <vector>
class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> res;

        for (int i = 0; i < strs.size(); i++) {
            string sorted = strs[i];
            sort(sorted.begin(), sorted.end());
            res[sorted].push_back(strs[i]);
        }

        vector<vector<string>> result;
        for (auto &pair : res) {
            result.push_back(pair.second);
        }

        return result;
    }
};
