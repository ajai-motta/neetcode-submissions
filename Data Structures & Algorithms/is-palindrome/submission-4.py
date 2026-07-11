class Solution:
    def isPalindrome(self, s: str) -> bool:
        lit=''.join(i.lower() for i in s if i.isalnum())
        if lit == ''.join(reversed(lit)):
            return True
        else:
            return False
        
        