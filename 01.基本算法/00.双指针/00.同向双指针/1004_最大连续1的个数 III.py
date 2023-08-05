class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans, left, cnt_0 = 0, 0, 0
        for right, num in enumerate(nums):
            cnt_0 += 1 - num
            while left <= right and cnt_0 > k:
                cnt_0 -= 1 - nums[left]
                left += 1
            ans = max(ans, right - left + 1)
        return ans