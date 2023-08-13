class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xorResult = 0
        for num in nums:
            xorResult ^= num
        
        lowbit = xorResult & (-xorResult)  # 取二进制表示小最右侧的 1
        
        type1, type2 = 0, 0
        for num in nums:
            if lowbit & num == 0:
                type1 ^= num
            else:
                type2 ^= num
        return [type1, type2]