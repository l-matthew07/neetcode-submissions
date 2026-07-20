class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = list(c.lower() for c in s if c.isalnum())
        left = 0
        right = len(string) - 1
        while left <= right:
            if string[left] != string[right]:
                return False
            else:
                left += 1
                right -= 1
        return True