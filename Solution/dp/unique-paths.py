class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # space O(n * m) this is faster accd to leetcode but same time complexity
        # dp = [ [ 0 for _ in range(n+1) ] for _ in range(m+1) ]
        # for i in reversed(range(m)):
        #     for j in reversed(range(n)):
        #         if i == m-1 and j == n-1:
        #             dp[i][j] = 1
        #             continue
        #         dp[i][j] = dp[i+1][j] + dp[i][j+1]
                                
        # return dp[0][0]

        # space O(n)
        row = [1] * n  # bottom-most row

        for i in range(m - 1):
            tmp = [1] * n
            for j in reversed(range(n - 1)):
                tmp[j] = tmp[j + 1] + row[j] # row[j] essentially has the value of row below wrt to first sol
            row = tmp

        return row[0]

