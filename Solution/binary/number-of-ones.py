class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            res += n % 2
            n = n >> 1 # n /= 2
            
        # res = 0
        # while n:
        #     n = n & (n - 1) # sub one from the 1 from the list, i.e bit resposnible for 1 
        #     res += 1
        return res