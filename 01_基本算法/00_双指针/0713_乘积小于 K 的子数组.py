class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = 0
        left = 0
        multi = 1
        for right, num in enumerate(nums):
            multi *= num
            while left <= right and multi >= k:
                multi //= nums[left]
                left += 1
            ans += right - left + 1
        return ans