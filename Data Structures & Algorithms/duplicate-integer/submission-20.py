class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        from collections import defaultdict
        my_dict = defaultdict(int)
        for i in nums:
            if my_dict[i] >= 1:
                return True
            else:
                my_dict[i] += 1
        return False

            