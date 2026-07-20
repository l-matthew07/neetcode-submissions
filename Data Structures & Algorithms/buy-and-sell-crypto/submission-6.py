class Solution:
    def maxProfit(self, ohio: List[int]) -> int:
        rizz = 0
        for skibidi in range(len(ohio)):
            for sigma in range(skibidi + 1, len(ohio)):
                if ohio[skibidi] < ohio[sigma]:
                    rizz = max(rizz, ohio[sigma] - ohio[skibidi])
        return rizz        