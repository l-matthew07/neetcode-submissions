class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        max_length = 0
        letters = {}
        for end in range(len(s)):
            if s[end] in letters and letters[s[end]] >= start:
                start = letters[s[end]] + 1
            letters[s[end]] = end
            max_length = max(max_length, end - start + 1)
        
        return max_length