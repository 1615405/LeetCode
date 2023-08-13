class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        '''
        f(i) = max{f(i-1) + nums[i], nums[i]}
        n = len(nums)
        dp = [0 for _ in range(n)]

        dp[0] = nums[0]
        for i in range(1, n):
            dp[i] = max(nums[i], dp[i - 1] + nums[i])
        return max(dp)
        '''
        n = len(nums)
        last = 0
        ans = -inf
        for i in range(n):
            last = nums[i] + max(last, 0)
            ans = max(last, ans)
        return ans