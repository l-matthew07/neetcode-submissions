#include <iostream>
#include <vector>
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> seen;
        for (int i = 0; i < nums.size(); i++){
            int need = target-nums[i];
            if (seen.find(need) != seen.end()){
                int j = seen[need];
                return {j, i};
            }
            seen[nums[i]] = i;
        }
    }
};
