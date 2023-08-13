class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        ans = n + 1  # inf
        left = 0
        interval_sum = 0
        for right, x in enumerate(nums):
            interval_sum += x
            while interval_sum >= target and left <= right:
                ans = min(ans, right - left + 1)
                interval_sum -= nums[left]
                left += 1
        return ans if ans <= n else 0