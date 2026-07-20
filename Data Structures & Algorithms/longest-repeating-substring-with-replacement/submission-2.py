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
                left_char = s[left]
                char_count[left_char] -= 1
                left += 1
            
            max_len = max(max_len, right - left + 1)
        
        return max_len
        
            