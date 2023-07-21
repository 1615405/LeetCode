class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = 0
        left = 0
        multi = 1
        for right, num in enumerate(nums):
            multi *= num
            while left <= right and multi >= k:
                multi //= nums[left]
                left += 1
            ans += right - left + 1
        return ans



class Solution {
public:
    int numSubarrayProductLessThanK(vector<int>& nums, int k) {
        int ans = 0, multi = 1, left = 0;
        for (int right = 0; right < nums.size(); right++) {
            multi *= nums[right];
            while (left <= right && multi >= k) {
                multi /= nums[left];
                left++;
            }
            ans += right - left + 1;
        }
        return ans;
    }
};