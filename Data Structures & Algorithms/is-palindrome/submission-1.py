class Solution:
    def isPalindrome(self, s: str) -> bool:
        ch=""
        for a in s:
            if a.isalnum():
                ch += a.lower()
        return ch == ch[::-1]
        
        

        
        
                     