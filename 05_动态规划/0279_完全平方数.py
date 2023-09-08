'''
class Solution:
    def numSquares(self, n: int) -> int:
        nums = []
        i = 1
        while i * i <= n:
            nums.append(i * i)
            i += 1
        
        target = n
        length = len(nums)
        dp = [[target + 1] * (target + 1) for _ in range(length + 1)]
        dp[0][0] = 0

        for i in range(1, length + 1):
            for j in range(target + 1):
                if j < nums[i - 1]:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - nums[i - 1]] + 1)
        
        return dp[length][target]
'''


class Solution:
    def numSquares(self, n: int) -> int:
        f = [inf] * (n + 1)
        f[0] = 0
        m = isqrt(n) + 1
        for i in range(1, m):
            x = i * i
            for j in range(x, n + 1):
                f[j] = min(f[j], f[j - x] + 1)
        return f[n]