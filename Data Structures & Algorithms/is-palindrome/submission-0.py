class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered = [c.lower() for c in s if c.isalnum()]
        if filtered == filtered[::-1]:
            return True
        else:
            return False