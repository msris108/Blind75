class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        
        for i in range(32):
            bit = (n >> i) & 1 # shift the number by i bits and & to get the last bit
            res = res | (bit << (31 - i)) # set (use OR) that bit in reverse order (31 - i)
            
        return res