class Solution:
    
    def isPalindrome(self, s: str) -> bool:
        newstr = ""
        
        for c in s:
            if c.isalnum():
                newstr += c.lower()
        
        def check(s):
            l, r = 0, len(s) - 1
            while l <= r:
                if s[l] == s[r]:
                    l += 1
                    r -= 1
                else:
                    return False
                
            return True
            
        
        return check(newstr) # return newstr == newstr[::-1]