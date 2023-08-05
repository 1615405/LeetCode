class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            pivot = (left + right) // 2
            if nums[pivot] == nums[right]:
                right -= 1
            elif nums[pivot] > nums[right]:
                left = pivot + 1
            else:
                right = pivot
        return nums[left]