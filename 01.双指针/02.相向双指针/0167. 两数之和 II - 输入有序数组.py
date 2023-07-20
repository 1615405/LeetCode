class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        while left < right:
            s = numbers[left] + numbers[right]
            if s == target:
                break
            if s < target:
                left += 1
            elif s > target:
                right -= 1
        return [left + 1, right + 1]




class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int left = 0, right = numbers.size() - 1;
        while (left < right) {
            int x = numbers[left] + numbers[right];
            if (x < target) {
                left++;
            } else if (x > target) {
                right--;
            } else {
                break;
            }
        }
        return {left + 1, right + 1};
    }
};