class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def is_blue(i: int) -> bool:
            if nums[i] > nums[-1]:
                return target > nums[-1] and nums[i] >= target
            else:
                return nums[i] >= target or target > nums[-1]
        
        left, right = 0, len(nums) - 1
        while left < right:
            pivot = (left + right) // 2
            if is_blue(pivot):
                right = pivot
            else:
                left = pivot + 1
        return left if left < len(nums) and nums[left] == target else -1



class Solution {
public:
    int search(vector<int>& nums, int target) {
        function<int(int)> is_blue = [&](int i) -> bool {
            int len = nums.size();
            if (nums[i] > nums[len - 1]) {
                return nums[i] >= target && target > nums[len - 1];
            } else {
                return nums[i] >= target || target > nums[len - 1];
            }
        };
        int left = 0, right = nums.size() - 1;
        while (left < right) {
            int pivot= left + (right - left) / 2;
            if (is_blue(pivot)) {
                right = pivot;
            } else {
                left = pivot + 1;
            }
        }
        if (left == (int)nums.size() || nums[left] != target) {
            return -1;
        }
        return left;
    }
};