class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_len = 0
        max_count = 0
        left = 0
        char_count = {}
        
        for right in range(len(s)):
            char = s[right]
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
            
            max_count = max(max_count, char_count[char])
            
            while (right - left + 1) - max_count > k:
                char_count[s[left]] -= 1
                left += 1
            
            
        
        return (right - left + 1)
        
            