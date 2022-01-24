class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        res_len = 0
        for i in range(len(s)):
            # odd length palindrome expand from center (i)
            l, r = i, i
            while l >= 0 and r <= len(s)-1 and s[l] == s[r]:
                if(r - l + 1 > res_len):
                    res_len = r - l + 1
                    res = s[l:r+1]
                l-=1
                r+=1
            
            # even length palindrome expand from center (i) and center + 1 (i + 1)
            l, r = i, i+1
            while l >= 0 and r <= len(s)-1 and s[l] == s[r]:
                if(r - l + 1 > res_len):
                    res_len = r - l + 1
                    res = s[l:r+1]
                l-=1
                r+=1
                    
        return res