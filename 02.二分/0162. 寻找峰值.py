class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[mid + 1]:  # 答案在[left, mid]区间中
                right = mid
            else:
                left = mid + 1  # 答案在[left + 1, right]区间中
        return left




class Solution {
public:
    int findPeakElement(vector<int>& nums) {
        // 二分答案
        int left = 0, right = nums.size() - 1;
        while (left < right) {
            int mid = left + (right - left) / 2;
            if (nums[mid] > nums[mid + 1]) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }
        return left;
    }
};