class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int minPrice = prices[0];
        int maxProfit = 0;
        
        for (int i = 1; i < prices.size(); i++) {
            // Update max profit if selling at current price
            maxProfit = max(maxProfit, prices[i] - minPrice);
            // Update minimum price seen so far
            minPrice = min(minPrice, prices[i]);
        }
        
        return maxProfit;
    }
};