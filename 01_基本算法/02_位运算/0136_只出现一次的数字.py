class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        single = 0
        for x in nums:
            single ^= x
        return single