def lower_bound(nums: List[int], target: int) -> int:
    left, right = 0, len(nums)
    while left < right:
        pivot = (left + right) // 2
        if nums[pivot] >= target:
            right = pivot
        else:
            left = pivot + 1
    return left

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
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
        '''




class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        function<int(void)> bsearch_1 = [&](void) -> int {
            int left = 0, right = nums.size() - 1;
            while (left < right) {
                int pivot = left + (right - left) / 2;
                if (nums[pivot] >= target) {
                    right = pivot;
                } else {
                    left = pivot + 1;
                }
            }
            return left;
        };
        
        function<int(void)> bsearch_2 = [&](void) -> int {
            int left = 0, right = nums.size() - 1;
            while (left < right) {
                int pivot = left + (right - left) / 2 + 1;
                if (nums[pivot] > target) {
                    right = pivot - 1;
                } else {
                    left = pivot;
                }
            }
            return left;
        };

        int x = bsearch_1();
        int y = bsearch_2();
        
        if (x == (int)nums.size() || nums[x] != target) {
            return vector<int>{-1, -1};
        }
        return vector<int>{x, y};
    }
};