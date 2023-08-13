def majorityElement(self, nums: List[int]) -> int:
    # Boyer-Moore 投票算法
    # 时间复杂度 O(n)
    # 空间复杂度 O(n)
    count = 0
    candidate = None
    for num in nums:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)
    return candidate