class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans, left = 0, 0
        for right, x in enumerate(nums):
            while x - nums[left] > 2 * k and left <= right:
                left += 1
            ans = max(ans, right - left + 1)
        return ans




class Solution {
public:
    int maximumBeauty(vector<int>& nums, int k) {
        sort(nums.begin(), nums.end());
        int ans = 0, left = 0;
        for (int right = 0; right < nums.size(); right++) {
            while (left <= right && nums[right] - nums[left] > 2 * k) {
                left++;
            }
            ans = max(ans, right - left + 1);
        }
        return ans;
    }
};