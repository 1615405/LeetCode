class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            pivot = (left + right) // 2
            if nums[pivot] == nums[right]:
                right -= 1
            elif nums[pivot] > nums[right]:
                left = pivot + 1
            else:
                right = pivot
        return nums[left]




class Solution {
public:
    int findMin(vector<int>& nums) {
        int left = 0, right = nums.size() - 1;
        while (left < right) {
            int pivot = left + (right - left) / 2;
            if (nums[pivot] < nums[right]) {
                right = pivot;
            } else if (nums[pivot] == nums[right]) {
                right--;
            } else {
                left = pivot + 1;
            }
        }
        return nums[left];
    }
};