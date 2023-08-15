class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        while left < right:
            s = numbers[left] + numbers[right]
            if s == target:
                break
            if s < target:
                left += 1
            elif s > target:
                right -= 1
        return [left + 1, right + 1]