def lower_bound(nums: List[int], target: int) -> int:
    left, right = 0, len(nums)
    while left < right:
        pivot = (left + right) // 2
        if nums[pivot] >= target:
            right = pivot
        else:
            left = pivot + 1
    return left

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = lower_bound(nums, target)
        if start == len(nums) or nums[start] != target:
            return [-1, -1]
        end = lower_bound(nums, target + 1) - 1
        return [start, end]



class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = bisect_left(nums, target)
        if start == len(nums) or nums[start] != target:
            return [-1, -1]
        end = bisect_right(nums, target) - 1
        return [start, end]