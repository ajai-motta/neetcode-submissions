class Solution:
    def isPalindrome(self, s: str) -> bool:
        lit=''.join(i.lower() for i in s if i.isalnum())
        return lit == lit[::-1]
        
        