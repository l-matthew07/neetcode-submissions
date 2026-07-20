class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_of = {}                     
        for i, x in enumerate(nums):
            comp = target - x
            if comp in index_of:
                y = index_of[comp]
                return [y, i]
            index_of[x] = i        
        return None