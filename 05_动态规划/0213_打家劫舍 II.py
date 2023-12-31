class Solution:
    def rob(self, nums: List[int]) -> int:
        def my_rob(nums: List[int]) -> int:
            cur, pre = 0, 0
            for num in nums:
                cur, pre = max(pre + num, cur), cur
            return cur
        
        return max(my_rob(nums[:-1]), my_rob(nums[1:])) if len(nums) != 1 else nums[0]