class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        ans = []
        for i in range(n - 2):
            x = nums[i]
            if i > 0 and nums[i - 1] == x:
                continue
            if x + nums[-2] + nums[-1] < 0:
                continue
            if x + nums[i] + nums[i + 1] > 0:
                break
            left = i + 1
            right = n - 1
            while left < right:
                s = x + nums[left] + nums[right]
                if s > 0:
                    right -= 1
                elif s < 0:
                    left += 1
                else:
                    ans.append([x, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
                    while nums[right] == nums[right + 1] and left < right:
                        right -= 1
        return ans