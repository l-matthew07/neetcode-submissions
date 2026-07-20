class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import defaultdict
        res = []
        my_dict = defaultdict(int)
        for i in nums: 
            my_dict[i] += 1
        for i in range(k):
            key=(max(my_dict, key=my_dict.get))
            res.append(key)
            del my_dict[key]
        return res