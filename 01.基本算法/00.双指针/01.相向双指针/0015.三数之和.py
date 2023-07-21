class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        ans = []
        for i in range(n - 2):
            x = nums[i]
            if i > 0 and nums[i - 1] == x:
                continue
            if x + nums[-2] + nums[-1] < 0:
                continue
            if x + nums[i] + nums[i + 1] > 0:
                break
            left = i + 1
            right = n - 1
            while left < right:
                s = x + nums[left] + nums[right]
                if s > 0:
                    right -= 1
                elif s < 0:
                    left += 1
                else:
                    ans.append([x, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
                    while nums[right] == nums[right + 1] and left < right:
                        right -= 1
        return ans




class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        int n = nums.size();
        sort(nums.begin(), nums.end());
        vector<vector<int>> ans;
        for (int i = 0; i < nums.size() - 2; i++) {
            if (i > 0 && nums[i] == nums[i - 1]) {
                continue;
            }
            if (nums[i] + nums[n - 1] + nums[n - 2] < 0) {
                continue;
            }
            if (nums[i] + nums[i + 1] + nums[i + 2] > 0) {
                break;
            }
            int left = i + 1, right = n - 1;
            while (left < right) {
                int s = nums[i] + nums[left] + nums[right];
                if (s < 0) {
                    left++;
                } else if (s > 0) {
                    right--;
                } else {
                    ans.push_back({nums[i], nums[left], nums[right]});
                    left++;
                    right--;
                    while (nums[left] == nums[left - 1] && left < right) {
                        left++;
                    }
                    while (nums[right] == nums[right + 1] && left < right) {
                        right--;
                    }
                }
            }
        }
        return ans;
    }
};