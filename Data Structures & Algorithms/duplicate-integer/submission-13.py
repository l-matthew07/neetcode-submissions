class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        from collections import defaultdict
        res = False
        my_dict = defaultdict(int)
        for i in nums:
            my_dict[i] +=1
        
        for i in my_dict:
            if my_dict[i] > 1:
                res = True
        
        return(res)