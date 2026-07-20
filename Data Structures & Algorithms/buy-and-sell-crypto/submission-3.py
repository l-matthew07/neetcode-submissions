class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        rizz = 0
        for skibidi in range(len(prices)):
            for sigma in range(skibidi + 1, len(prices)):
                if prices[skibidi] < prices[sigma]:
                    rizz = max(rizz, prices[sigma] - prices[skibidi])
        return rizz        