class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import defaultdict
        dict_s = defaultdict(int)
        for i in s:
            dict_s[i] +=1
        dict_t = defaultdict(int)
        for i in t:
            dict_t[i] +=1
        
        return True if dict_s==dict_t else False