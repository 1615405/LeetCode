class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        n, target = len(nums), sum(nums) - x
        ans, left, s, flag = 0, 0, 0, 0
        for right, num in enumerate(nums):
            s += num
            while left <= right and s > target:
                s -= nums[left]
                left += 1
            if s == target:
                ans = max(ans, right - left + 1)
                flag = 1
        if flag == 0:
            return -1
        return n - ans




class Solution {
public:
    int minOperations(vector<int>& nums, int x) {
        int target = accumulate(nums.begin(), nums.end(), 0) - x;
        if (target < 0) {
            return -1;
        }
        int ans = -1, left = 0, sum = 0, n = nums.size();
        for (int right = 0; right < n; right++) {
            sum += nums[right];
            while (sum > target && left <= right) {
                sum -= nums[left];
                left++;
            }
            if (sum == target) {
                ans = max(ans, right - left + 1);
            }
        }
        return ans < 0 ? -1 : n - ans;
    }
};