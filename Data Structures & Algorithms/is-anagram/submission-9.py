class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        first_dict = {}
        for i in s:
            first_dict[i] = 1 + first_dict.get(i, 0)
        second_dict = {}
        for n in t:
            second_dict[n] = 1 + second_dict.get(n, 0)
        if first_dict == second_dict:
            return True
        return False