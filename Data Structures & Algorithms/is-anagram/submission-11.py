class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        for i in s:
            s_dict[i] = 1 + s_dict.get(i, 0)
        
        t_dict = {}
        for n in t:
            t_dict[n] = 1 + t_dict.get(n, 0)
        
        if s_dict == t_dict:
            return True
        else:
            return False