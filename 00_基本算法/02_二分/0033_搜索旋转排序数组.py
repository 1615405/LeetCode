class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def is_blue(i: int) -> bool:
            if nums[i] > nums[-1]:
                return target > nums[-1] and nums[i] >= target
            else:
                return nums[i] >= target or target > nums[-1]
        
        left, right = 0, len(nums) - 1
        while left < right:
            pivot = (left + right) // 2
            if is_blue(pivot):
                right = pivot
            else:
                left = pivot + 1
        return left if left < len(nums) and nums[left] == target else -1