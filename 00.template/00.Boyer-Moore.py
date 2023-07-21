class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Boyer-Moore 投票算法
        # 时间复杂度 O(n)
        #  空间复杂度 O(n)
        count = 0
        candidate = None
        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)
        return candidate




class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int count = 0, candidate = -1;
        for (int num : nums) {
            if (count == 0) {
                candidate = num;
            }
            count += (num == candidate) ? 1 : -1;
        }
        return candidate;
    }
};