def lower_bound(nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        '''
        start = lower_bound(nums, target)
        if start == len(nums) or nums[start] != target:
            return [-1, -1]
        end = lower_bound(nums, target + 1) - 1
        return [start, end]
        '''
        start = bisect_left(nums, target)
        if start == len(nums) or nums[start] != target:
            return [-1, -1]
        end = bisect_right(nums, target) - 1
        return [start, end]




class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        if (nums.empty()) {
            return {-1, -1};
        }
        int left = 0, right = nums.size() - 1;
        int index1 = -1, index2 =-1;
        while (left < right) {
            int mid = left + (right - left) / 2;
            if (nums[mid] >= target) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }
        index1 = left;

        left = 0, right = nums.size() - 1;
        while (left < right) {
            int mid = left + (right - left) / 2 + 1;
            if (nums[mid] > target) {
                right = mid - 1;
            } else {
                left = mid;
            }
        }
        index2 = left;
        
        if (nums[index1] != target || nums[index2] != target) {
            return {-1, -1};
        }
        return {index1, index2};
    }
};