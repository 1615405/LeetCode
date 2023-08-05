class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        n, target = len(nums), sum(nums) - x
        ans, left, s, flag = 0, 0, 0, 0
        for right, num in enumerate(nums):
            s += num
            while left <= right and s > target:
                s -= nums[left]
                left += 1
            if s == target:
                ans = max(ans, right - left + 1)
                flag = 1
        if flag == 0:
            return -1
        return n - ans