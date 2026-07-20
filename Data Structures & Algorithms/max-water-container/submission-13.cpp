#include <algorithm>
class Solution {
public:
    int maxArea(vector<int>& heights) {
        int max = 0;

        for (int i = 0; i < heights.size(); i++){
            int r = heights.size()-1;
            while (i<r) {
            int height = std::min(heights[i], heights[r]);
            int area = (r-i)*height;
            if (area > max) {
                max = area;
            }
            r -= 1;
        }
        }
        return max;
    }
};