class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        max_length = 0
        used_chars = set()
    
        for end in range(len(s)):
            while s[end] in used_chars:
                used_chars.remove(s[start])
                start += 1
            used_chars.add(s[end])
            max_length = max(max_length, end - start + 1)
    
        return max_length