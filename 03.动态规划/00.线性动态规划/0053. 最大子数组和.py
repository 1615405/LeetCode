class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        '''
        f(i) = max{f(i-1) + nums[i], nums[i]}
        n = len(nums)
        dp = [0 for _ in range(n)]

        dp[0] = nums[0]
        for i in range(1, n):
            dp[i] = max(nums[i], dp[i - 1] + nums[i])
        return max(dp)
        '''
        n = len(nums)
        last = 0
        ans = -inf
        for i in range(n):
            last = nums[i] + max(last, 0)
            ans = max(last, ans)
        return ans



class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        /*
        int n = nums.size();
        vector<int> dp(n, -1);
        dp[0] = nums[0];
        for (int i = 1; i < n; i++) {
            dp[i] = max(nums[i], dp[i - 1] + nums[i]);
        }
        int ans = INT_MIN;
        for (int i = 0; i < n; i++) {
            ans = max(ans, dp[i]);
        }
        return ans;
        */
        int n = nums.size(), last = 0, ans = INT_MIN;
        for (int i = 0; i < n; i++) {
            last = nums[i] + max(last, 0);
            ans = max(ans, last);
        }
        return ans;
    }
};