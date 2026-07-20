from collections import defaultdict

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_count = defaultdict(int)
        for i in nums:
            if nums_count[i] >=1:
                return True
            else:
                nums_count[i] +=1
        return False